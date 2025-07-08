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
week_counter=0

while (( weekday_commits < 60 )); do
    day_of_week=$(date --date="$days_back days ago" +%u)  # 1=Mon, ..., 7=Sun

    if [[ "$day_of_week" -lt 6 ]]; then  # Weekday
        # Start of a new week? Reset skip control
        if (( weekday_commits % 5 == 0 )); then
            skip_day=$(( RANDOM % 5 ))  # Randomly skip one weekday this week (0–4)
            skipped_today=0
        fi

        # Skip this day if it matches the random skip
        if (( (weekday_commits % 5) == skip_day )); then
            echo "🚫 Skipping weekday $((weekday_commits + 1)) for realism"
            ((weekday_commits++))
            ((days_back++))
            continue
        fi

        # Random number of commits (1–3) on this day
        commits_today=$(( (RANDOM % 3) + 1 ))

        for ((c=1; c<=commits_today; c++)); do
            num_files=$(( (RANDOM % 6) + 1 ))  # 1–6 files
            commit_files=()

            for ((j=0; j<num_files; j++)); do
                if (( file_index >= total_files )); then break; fi
                file="${all_files[$file_index]}"
                commit_files+=("$file")
                ((file_index++))
            done

            # Randomly modify one of the files (~20%)
            if (( RANDOM % 5 == 0 )) && [[ -f "${commit_files[0]}" ]]; then
                echo "// ✏️ Edited on simulated weekday $((weekday_commits + 1))" >> "${commit_files[0]}"
            fi

            # Randomly delete a file (~10%)
            if (( RANDOM % 10 == 0 )); then
                rand_del_index=$(( RANDOM % total_files ))
                del_file="${all_files[$rand_del_index]}"
                if [[ -f "$del_file" ]]; then
                    rm "$del_file"
                    git rm "$del_file"
                    echo "🗑️ Deleted $del_file"
                fi
            fi

            # Simulated commit time
            hour=$(( RANDOM % 8 + 10 ))  # 10 AM to 5 PM
            commit_date=$(date --date="$days_back days ago $hour:00" +"%Y-%m-%dT%H:%M:%S")

            # Commit
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
