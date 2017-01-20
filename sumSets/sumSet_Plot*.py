import sumSet
import subprocess
import sys
import fileinput


sumSet.main()
L = [(x,y) for x in range(4) for y in range(x,4)]
for x in L:
    with fileinput.FileInput('1test_input.txt', inplace=True) as file:
        for line in file:
            if "output" in line:
                print(line.replace(line, 'set output' + " 'z" + str(x) + ".png'"))
            elif "plot" in line:
                print(line.replace(line, "plot [0:100] [0:100]" + " '" + str(x) + ".txt' " + "using ($1 + .5):($2 + .5):( $3 == 0 ? 0 : 1 ) with points pt 5 ps 1.5 palette"), end ="")
            else:
                print(line, end="")
    cmd = ' '.join(['gnuplot', '~/workspace/NewMathCode/Misere/sumSets/1test_input.txt'])
    subprocess.check_output(cmd, shell=True)

# def main():
#     input_file = sys.argv[1]
#     nDimSubGame.DO_WORK(input_file)
#
#
# if __name__ == '__main__':
#     main()

# example driver
# for input_file in ['test.txt', 'blah.txt']:
#     nDimSubGame.DO_WORK_HERE(input_file)
#     cmd = ' '.join(['gnuplot', '~/workspace/NewMathCode/Misere/1MisereGraph_input.txt'])
#     subprocess.check_output(cmd, shell=True)
#     cmd2 = ' '.join(['eog', '~/workspace/NewMathCode/Misere/MiserePlot7.png'])
#     subprocess.check_output(cmd2, shell=True)
