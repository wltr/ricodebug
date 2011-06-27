# ricodebug - A GDB frontend which focuses on visually supported
# debugging using data structure graphs and SystemC features.
#
# Copyright (C) 2011  The ricodebug project team at the
# Upper Austrian University Of Applied Sciences Hagenberg,
# Department Embedded Systems Design
#
# This file is part of ricodebug.
#
# ricodebug is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# For further information see <http://syscdbg.hagenberg.servus.at/>.

from PyQt4.QtCore import QObject

class VariableList(QObject):
    """
    holds variablewrappers that are generated by the given factory
    """
    
    def __init__(self, factory, distributedObjects):
        """ Constructor
        @param factory               variables.varwrapperfactory.VarWrapperFactory,
                                     WrapperFactory of the Module using the VariableList
        @param distributedObjects    distributedobjects.DistributedObjects, the DistributedObjects-Instance """
        QObject.__init__(self)
        self.varPool = distributedObjects.variable_pool
        self.factory = factory
        self.list = []
        
    def addVarByName(self, varName):
        """ adds new VariableWrapper for given varName and returns this newly added VariableWrapper
        @param varName    string, the name of the Variable to add  """
        var = self.varPool.getVar(str(varName))
        if var != None:
            vw = var.makeWrapper(self.factory)
            self.list.append(vw)
            return vw
        return var
    
    def addVar(self, varWrapper):
        """ adds VariableWrapper varWrapper to the list
        @param varWrapper    variables.variablewrapper.VariableWrapper, VariableWrapper to add to the list """
        self.list.append(varWrapper)
        
    def addLocals(self):
        for var in self.varPool.addLocals():
            vw = var.makeWrapper(self.factory)
            self.list.append(vw)
    
    def removeVar(self, varWrapper):
        """ removes VariableWrapper varWrapper from the list
        @param varWrapper    variables.variablewrapper.VariableWrapper, VariableWrapper to remove from the list """
        self.list.remove(varWrapper)
    
    def clear(self):
        """ Clears the whole VariableList. """
        self.list = []
        
    def replaceVar(self, oldVar, newVar):
        #vw = self.list[self.list.index(oldVar)]
        #vw.variable = newVar
        vw = newVar.makeWrapper(self.factory)
        self.list[self.list.index(oldVar)] = vw
        return vw
        
    def getVariableWrapper(self, var):
        return self.list[self.list.index(var)]
        
    def __getitem__(self, key):
        return self.list[key]
    
    def __setitem__(self, key, item):
        self.list[key] = item
    
    def __len__(self):
        return len(self.list)
    
    def __delitem__(self, key):
        del self.list[key]
