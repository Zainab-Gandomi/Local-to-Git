import subprocess

def main():
    proc = subprocess.Popen(['hdfs', 'dfs','-copyFromLocal', 
                            '/directory/file name',
                            'hdfs:///directory inside hdfs'],
                             stdout = subprocess.PIPE,
                             stderr = subprocess.PIPE)

main()