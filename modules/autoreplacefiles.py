import os
import glob
import shutil

os.chdir("..")
cur_dir = os.path.abspath(os.curdir)

os.chdir(cur_dir)
for file in glob.glob("*.*"):
    if file == 'user_config.ini':
        print("[Skipped] : " + file)
    else:
        print("[Deleted] : " + file)
        os.remove(file)

os.chdir("./modules")
for file in glob.glob("*.*"):
    if file == 'autoreplacefiles.py':
        print("[Skipped] : " + file)
    else:
        print("[Deleted] : " + file)
        os.remove(file)

os.chdir("..")
os.chdir("./League-of-Locales-master")
lo_locale_dir = os.path.abspath(os.curdir)

for file in glob.glob("*.*"):
    if file == 'autoreplacefiles.py':
        print("[Skipped] : " + file)
    else:
        print("[Copying] : " + file)
        shutil.copy(file, cur_dir)

os.chdir("..")
os.chdir("./modules")
modules_dir = os.path.abspath(os.curdir)
# print(modules_dir)

os.chdir("..")
os.chdir(lo_locale_dir)
os.chdir("./modules")
lo_locale_modules = os.path.abspath(os.curdir)
# print(lo_locale_modules)
for file in glob.glob("*.*"):
    if file == 'autoreplacefiles.py':
        print("[Skipped] : " + file)
    else:
        print("[Copying] : " + file)
        shutil.copy(file, modules_dir)

print("Cleaning up...", end="")
os.chdir(cur_dir)
shutil.rmtree("League-of-Locales-master")
print("Done!")
print("Update complete!\nRestarting...")
os.system("start /B start cmd.exe @cmd /k py leagueoflocales.py")
exit()
