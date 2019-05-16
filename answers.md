* What are the key features of the application? Are these clearly separated into their own files, classes, and/or modules?
  * Creating a Histogram
    * Listogram
    * Dictogram
  * Sampling a Histogram
    * In my project currently only with ditcograms, but not a lot of change to change to listogram
  * They are seperated, but could be done better

* Are the names of files, modules, functions, and variables appropriate and accurate? Would a new programmer be able to understand the names without too much contextual knowledge?
  * Before the refactor, I don't think a new programmer with no context would understand the names

* What are the scopes of variables and are they appropriate for their use case? If there are global variables, why are they needed?
  * I didn't actually use any global variables, they are all scoped to the functions
  * all of the variable scopes are to the function

* Are the functions small and clearly specified, with as few side effects as possible?
  * I belive it is broken down into parts pretty well

* Are there functions that could be better organized in an Object-Oriented Programming style by defining them as methods of a class?
  * all of the creating a histogram functions

* Can files be used as both modules and as scripts?
  * yes

* Do modules all depend on each other or can they be used independently?
  * With my implementation, they rely on each other
