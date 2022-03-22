### forward
in pytorch, when you use module, and you inherit module and create a new net, you will definite a forward function. Then you find that the forward will be mobilized if you aplly the net.    
    It is because that the net is inherited from the module, in module, there is a function named '__call__' which will mobilize the forward.
