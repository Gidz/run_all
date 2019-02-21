import os
import subprocess

#All the files that can't be run will be appended to this list
unknown_files = []

failed_scripts = 0
successful_scripts = 0

#Association map
# To support more types of scripts,
#Simply add the extension and which shell command will execute the extension here
associations = {
  # "file extension":"will be run by",
  "py":"python",
  "pl":"perl",
  "sh":"sh",
  "rb":"ruby",
}

def _run(executable,file):
    global failed_scripts
    global successful_scripts

    print("Running "+file+" . . .")
    print("----------------------")
    try:
        ret = subprocess.run([executable,file])
        if(ret.returncode==0):
            successful_scripts+=1
        else:
            failed_scripts+=1
    except:
        print(file, "failed to run")
        failed_scripts+=1
    print("")

def run(files_list):
    # Keep count of the number of scripts executed
    count = 0
    for file in files_list:
        # This script will be executed as well since it is in the directory.
        # Preventing this by a simple check.
        if not __file__==file:
            name_and_extension_list= file.split('.')
            if(len(name_and_extension_list)!=1):
                extension=name_and_extension_list[-1]
                executable = associations.get(extension,None)

                # If the extension has not associated runner, add it to the unknown files list
                if not executable:
                    unknown_files.append(file)
                else:
                    _run(executable, file)
                    count = count + 1
            else:
                # Add the files without an extension to unknown_files
                unknown_files.append(file)
    return count

def main():
    num_executed= run(os.listdir())

    print("RESULTS")
    print("---------")
    print("Attempted to execute",num_executed,"script(s)")
    print(successful_scripts,"script(s) succeeded.")
    print(failed_scripts,"script(s) failed.")
    
    print("")
    print(len(unknown_files),"file(s) with unknown extension(s).")
    for file in unknown_files:
        print('>', file)



if __name__=="__main__":
    main()
