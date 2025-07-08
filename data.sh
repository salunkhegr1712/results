#!/bin/bash

export GIT_AUTHOR_NAME="Ghanasham Rajaram Salunkhe"
export GIT_COMMITTER_NAME="Ghanasham Rajaram Salunkhe"
export GIT_AUTHOR_EMAIL="salunkhegr1712@gmail.com"
export GIT_COMMITTER_EMAIL="salunkhegr1712@gmail.com"

cd coding-practice-history || exit

all_files=($(ls *.java | sort -R))
total_files=${#all_files[@]}
file_index=0
commit_id=1
days_back=0
weekday_commits=0
skipped_weekdays=0

while (( weekday_commits < 60 )); do
    day_of_week=$(date --date="$days_back days ago" +%u)  # 1=Mon, ..., 7=Sun

    if [[ "$day_of_week" -lt 6 ]]; then  # Weekday
        # New week: skip one random weekday
        if (( weekday_commits % 5 == 0 )); then
            skip_day=$(( RANDOM % 5 ))  # Skip 0–4 of current 5 weekdays
        fi

        if (( (weekday_commits % 5) == skip_day )); then
            echo "🚫 Skipping weekday $((weekday_commits + 1)) for realism"
            ((weekday_commits++))
            ((days_back++))
            continue
        fi

        commits_today=$(( (RANDOM % 3) + 1 ))  # 1–3 commits today

        for ((c=1; c<=commits_today; c++)); do
            num_files=$(( (RANDOM % 6) + 1 ))  # 1–6 files
            commit_files=()

            for ((j=0; j<num_files; j++)); do
                if (( file_index >= total_files )); then break; fi
                file="${all_files[$file_index]}"
                commit_files+=("$file")
                ((file_index++))
            done

            # Modify one file occasionally
            if (( RANDOM % 5 == 0 )) && [[ -f "${commit_files[0]}" ]]; then
                echo "// ✏️ Edited on simulated weekday $((weekday_commits + 1))" >> "${commit_files[0]}"
            fi

            # Delete a file occasionally
            if (( RANDOM % 10 == 0 )); then
                rand_del_index=$(( RANDOM % total_files ))
                del_file="${all_files[$rand_del_index]}"
                if [[ -f "$del_file" ]]; then
                    rm "$del_file"
                    git rm "$del_file"
                    echo "🗑️ Deleted $del_file"
                fi
            fi

            # Generate realistic time between 10:00–18:00
            hour=$(( RANDOM % 9 + 10 ))      # 10 to 18
            minute=$(( RANDOM % 60 ))        # 0 to 59
            commit_date=$(date --date="$days_back days ago $hour:$minute" +"%Y-%m-%dT%H:%M:%S")

            git add "${commit_files[@]}" 2>/dev/null
            GIT_AUTHOR_DATE="$commit_date" GIT_COMMITTER_DATE="$commit_date" \
              git commit -m "[$commit_id] Day $((weekday_commits + 1)): Add ${#commit_files[@]} Java file(s)"

            ((commit_id++))
        done

        ((weekday_commits++))
    fi

    ((days_back++))

    if (( file_index >= total_files )); then
        echo "✅ All files committed after $weekday_commits weekdays."
        break
    fi
done

cd ..
git push
