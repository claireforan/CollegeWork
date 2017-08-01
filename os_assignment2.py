# CPU class that holds the current process
class CPU():
    def __init__(self):
        self._process = None
        
 
     
  
# Process class that holds the process ID, the quanta, state and whether there is I/O
class Process():
    def __init__(self, pid, quanta, io, state, priority):
        self._pid = pid
        self._quanta = quanta
        self._io = io
        self._state = state
        self._priority = priority
         
    def __str__(self):
        strg = "pid: %s, quanta, %s, io:, %s" % (self._pid, self._quanta, self._io)
        return strg

class Queue():
     def __init__(self, timeslice):
        self._queue = []
        self._timeslice = timeslice
        self._head = 0

     def getProcess(self):
        # Return process at the top of blocked queue
        return self._head
    
    def addProcess(self, process):
        self._queue += [process]

    def removeProcess(self):
        self._queue.pop(0)
        


 # Scheduler class that holds the queues, the process and the CPU       
class Scheduler():
    def __init__(self):
        self._queue4 = Queue(16)
        self._queue6 = Queue(64)
        self._queue8 = Queue(256)
        self._queue10 = Queue(1024)
        self._queue12 = Queue(4096)
        self._queue14 = Queue(16384)
        self._queue16 = Queue(65536)
        self._queue18 = Queue(262144)
        self._blockedQ = Queue(None)
        self._process = None
        self._cpu = CPU()
        self.run()
         
    def addProcess(self, process):
        # add process to ready queue
        self._readyQ.addProcess(process)
 
    def removeProcess(self):
        # remove process from ready queue
        self._readyQ.remove()
 
    def addBlockedProcess(self, process):
        # add process to blocked queue
        self._readyQ.addReadyProcess(process)
 
    def removeBlockedProcess(self):
        # remove process from blocked queue
        self._readyQ.remove()
 
    def getProcess(self):
        # return the current process
        return self._process

    def runProcess(self):
        # Runs current process and checks for I/O
        # Moves process to Blocked queue and then to Ready queue if I/O
        # Reduces the process's quanta
        while len(current_queue) != 0:
        self._process = self._readyQ.getProcess()
        self._process._quanta -= 1
        if self._process._io == True:
            self._blockedQ.addBlockedProcess(self._process)
            process = self.removeProcess()
            print("Waiting for I/O")
            self._process._state = "Blocked"
            self._readyQ.addProcess(process)
            self._process._state = "Ready"
        process = self.remove()
        print("Process running")
        if int(self._process._quanta) > 0:
            self._process._priority += 2
            self._readyQ.addProcess(process)
            print("Process returned to ready queue") 
        else:
            print("Process terminated")
