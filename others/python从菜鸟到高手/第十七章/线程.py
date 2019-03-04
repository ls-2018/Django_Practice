import threading

threading.Thread()


class MyThread(threading.Thread):

    def __init__(self, func, args, name=''):
        super().__init__(target=func, name=name, args=args)

    def run(self):
        self._target(*self._args)


    '''
        # 所有的成员变量  都以 _ 开头
        def __init__(self, group=None, target=None, name=None,
                 args=(), kwargs=None, *, daemon=None):
        assert group is None, "group argument must be None for now"
        if kwargs is None:
            kwargs = {}
        self._target = target
        self._name = str(name or _newname())
        self._args = args
        self._kwargs = kwargs
        if daemon is not None:
            self._daemonic = daemon
        else:
            self._daemonic = current_thread().daemon
        self._ident = None
        self._tstate_lock = None
        self._started = Event()
        self._is_stopped = False
        self._initialized = True
        self._stderr = _sys.stderr
        _dangling.add(self)
        
    def run(self):    
        try:
            if self._target:
                self._target(*self._args, **self._kwargs)
        finally:
            del self._target, self._args, self._kwargs
        
    '''