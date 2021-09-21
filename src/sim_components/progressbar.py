import sys


def update_progresswtime(progress, totime, operation, remainops):

    estime = totime * remainops
    barLength = 40  # Modify this to change the length of the progress bar
    status = ""
    if isinstance(progress, int):
        progress = float(progress)
        status = ('Estimated time to completion: {0}m {1}s'.format(int((estime-estime % 60)/60), int(estime % 60)))
    if not isinstance(progress, float):
        progress = 0
        status = "error: progress var must be float\r\n"
    if progress < 0:
        progress = 0
        status = "Halt...\r\n"
    if progress >= 1:
        progress = 1
        status = "{} Completed...\r\n".format(operation)
    block = int(round(barLength*progress))
    text = "\rPercent: [{0}] {1}% {2} ".format("#"*block + "-"*(barLength-block), round(progress*100, 3), status)

    sys.stdout.write(text)

    sys.stdout.flush()


def update_progress(progress, operation):
    barLength = 40  # Modify this to change the length of the progress bar dynamically
    status = ""
    if isinstance(progress, int):
        progress = float(progress)
    if not isinstance(progress, float):
        progress = 0
        status = "error: progress var must be float\r\n"
    if progress < 0:
        progress = 0
        status = "Halt...\r\n"
    if progress >= 1:
        progress = 1
        status = "{} Completed...\r\n".format(operation)
    block = int(round(barLength*progress))
    text = "\rPercent: [{0}] {1}% {2} ".format("#"*block + "-"*(barLength-block), round(progress*100, 3), status)

    sys.stdout.write(text)

    sys.stdout.flush()
