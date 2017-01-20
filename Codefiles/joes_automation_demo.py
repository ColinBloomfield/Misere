import nDimSubGame
import subprocess
import sys


nDimSubGame.main()
cmd = ' '.join(['gnuplot', '~/workspace/NewMathCode/Misere/1MisereGraph_input.txt'])
subprocess.check_output(cmd, shell=True)
cmd2 = ' '.join(['eog', '~/workspace/NewMathCode/Misere/MiserePlot7.png'])
subprocess.check_output(cmd2, shell=True)


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