import os
import shutil
import sys


def sortDirectory(directory, func=shutil.move):

    if not os.path.isdir(directory):
        return

    for root, dirs, files in os.walk(directory):
        for dir in dirs:
            if not os.path.exists(os.path.join(str(directory), "Directories")):
                os.makedirs(os.path.join(str(directory), "Directories"))
            func(os.path.join(root, os.path.splitext(dir)[0]), os.path.join(str(directory), "Directories "))
        for file in files:
            name, ext = os.path.splitext(file); ext = ext[1:]
            #print("name: " + name + ", ext: " + ext)
            if not os.path.exists(os.path.join(str(directory), ext)):
                os.makedirs(os.path.join(str(directory), ext))


            if os.path.exists(os.path.join(str(directory), ext, file)):
                count = 1
                for newFile in os.listdir(os.path.join(str(directory), ext, '')):
                    if name == "_".join(newFile.split('.')[0].split('_')[:-1]):
                        count += 1
                outfile = name+'_'+str(count)+'.'+ext
            else:
                outfile = file
            print('File:', os.path.join(root, file), '->', os.path.join(str(directory), ext, outfile))
            func(os.path.join(root, file), os.path.join(str(directory), ext, outfile))

    return 0


def main():
    flag = shutil.move
    return sortDirectory(input("file path here: "), flag)


if __name__ == '__main__':
    main()


def someCode():
    iAmGoodProgrammer = "Hello world"
    upperLimit = 10*24+4
    for x in range(upperLimit):
        print(iAmGoodProgrammer, str(x))

    return 1



