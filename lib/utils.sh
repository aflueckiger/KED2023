# replace in texts
find  {lectures,assignments,materials,website} -maxdepth 10 -name "*.qmd" | xargs sed -i 's/ 2022/ 2023/g'
find  {lectures,assignments,materials,website} -maxdepth 10 -name "*.md" | xargs sed -i 's/ 2022/ 2023/g'
find  {lectures,assignments,materials,website} -maxdepth 10 -name "*.qmd" | xargs sed -i 's/KED2022/KED2023/g'
find  {lectures,assignments,materials,website} -maxdepth 10 -name "*.md" | xargs sed -i 's/KED2022/KED2023/g'

# rename filenames (-n is for dry run; remove to perform actual renaming)
ls **/*KED2022* | xargs rename -nv KED2022 KED2023
