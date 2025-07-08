#!/bin/bash

export GIT_AUTHOR_NAME="Ghanasham Rajaram Salunkhe"
export GIT_COMMITTER_NAME="Ghanasham Rajaram Salunkhe"
export GIT_AUTHOR_EMAIL="salunkhegr1712@gmail.com"
export GIT_COMMITTER_EMAIL="salunkhegr1712@gmail.com"

cd coding-practice-history || exit

# Shuffle available .java files
all_files=($(ls *.java | sort -R))
total_files=${#all_files[@]}
file_index=0
commit_id=1

# Start from 60 days ago, skip Saturdays & Sundays
days_back=0
weekday_commits=0

while (( weekday_commits < 60 )); do
    commit_day=$(date --date="$days_back days ago" +%u)  # 1=Mon, ..., 7=Sun

    if [[ "$commit_day" -lt 6 ]]; then  # Weekday
        commits_today=$(( (RANDOM % 3) + 1 ))  # 1–3 commits

        for ((c=1; c<=commits_today; c++)); do
            num_files=$(( (RANDOM % 6) + 1 ))  # 1–6 files
            commit_files=()

            for ((j=0; j<num_files; j++)); do
                if (( file_index >= total_files )); then break; fi
                file="${all_files[$file_index]}"
                commit_files+=("$file")
                ((file_index++))
            done

            # Random modification (~20%)
            if (( RANDOM % 5 == 0 )) && [[ -f "${commit_files[0]}" ]]; then
                echo "// ✏️ Edited on simulated weekday $((weekday_commits + 1))" >> "${commit_files[0]}"
            fi

            # Random deletion (~10%)
            if (( RANDOM % 10 == 0 )); then
                rand_del_index=$(( RANDOM % total_files ))
                del_file="${all_files[$rand_del_index]}"
                if [[ -f "$del_file" ]]; then
                    rm "$del_file"
                    git rm "$del_file"
                    echo "🗑️ Deleted $del_file"
                fi
            fi

            # Commit time
            hour=$((RANDOM % 8 + 10))  # 10am–5pm
            commit_date=$(date --date="$days_back days ago $hour:00" +"%Y-%m-%dT%H:%M:%S")

            # Git commit
            git add "${commit_files[@]}" 2>/dev/null
            GIT_AUTHOR_DATE="$commit_date" GIT_COMMITTER_DATE="$commit_date" \
              git commit -m "[$commit_id] Day $((weekday_commits + 1)): Add ${#commit_files[@]} Java file(s)"

            ((commit_id++))
        done

        ((weekday_commits++))
    fi

    ((days_back++))

    # Safety exit
    if (( file_index >= total_files )); then
        echo "✅ All files used after $weekday_commits weekdays."
        break
    fi
done

cd ..
git push
