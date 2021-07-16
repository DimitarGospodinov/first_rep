import os
from pathlib import Path


def extract_files(dir):
    return [el for el in dir if os.path.isfile(el)]


def get_report_for_files_extensions(files):
    report = {}
    for file in files:
        file_name, file_extension = os.path.splitext(file)
        if file_extension not in report:
            report[file_extension] = []
        report[file_extension].append(file_name)
    return report


dir_content = os.listdir()
files = extract_files(dir_content)
report_info = get_report_for_files_extensions(files)


file_name = "my_report_result.txt"
desktop_path = os.path.join(os.path.join(os.environ["OneDrive"],"Desktop"),file_name)
print(desktop_path)
result_str = ""
for extension, file_names in sorted(report_info.items(), key=lambda x: x[0]):
    result_str += f".{extension}\n"
    for name in file_names:
        result_str += f"- - - {name}.{extension}\n"
with open(desktop_path, "w") as file:
    file.write(result_str)
