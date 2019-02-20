import os
import subprocess

## Shared variables
unknown_files = []
## End of shared variables

#Extension vs Executable map
extensions = {
  "py":"python",
  "pl":"perl",
  "sh":"sh",
}

def _run(executable,file):
    print("Running "+file+" . . .")
    print("----------------------")
    subprocess.run([executable,file])
    print("")

def run(files_list):
    count = 0
    for file in files_list:
        if not __file__==file:
            temp = file.split('.')
            if(len(temp)!=1):
                executable = extensions[temp[-1]]
                _run(executable, file)
                count = count + 1
            else:
                unknown_files.append(file)
    return count

def main():
     num_executed= run(os.listdir())
     print("Executed",num_executed,"script(s)")

if __name__=="__main__":
    main()
