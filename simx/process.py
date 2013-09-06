# Copyright (c) 2012. Los Alamos National Security, LLC. 

# This material was produced under U.S. Government contract DE-AC52-06NA25396
# for Los Alamos National Laboratory (LANL), which is operated by Los Alamos 
# National Security, LLC for the U.S. Department of Energy. The U.S. Government 
# has rights to use, reproduce, and distribute this software.  

# NEITHER THE GOVERNMENT NOR LOS ALAMOS NATIONAL SECURITY, LLC MAKES ANY WARRANTY, 
# EXPRESS OR IMPLIED, OR ASSUMES ANY LIABILITY FOR THE USE OF THIS SOFTWARE.  
# If software is modified to produce derivative works, such modified software should
# be clearly marked, so as not to confuse it with the version available from LANL.

# Additionally, this library is free software; you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License v 2.1 as published by the 
# Free Software Foundation. Accordingly, this library is distributed in the hope that 
# it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of 
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See LICENSE.txt for more details.

import util

class Process:
    """
    Base class for all processes in simx.
    Provides functionality for process oriented simulation
    *Needs more desscription*
    """

    def __init__(self,pid):
        self.pid = pid


    def wait_for(self, process):
        """
        Suspends process till the given process finishes
        executing. 
        """
        util.check_type(Process, process)

    
    def sleep(self, time):
        """
        Suspends for specified amount of time
        """
        pass


    def run(self): 
        """
        All classes that inherit from this class should
        define this method. This is the method that gets
        run when the process is activated
        """
        pass

        

    
            
        
