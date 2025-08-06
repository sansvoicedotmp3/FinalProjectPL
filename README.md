# Welcome to my Pokemon Damage Simulator!

This project is for my Programming Languages class. I wanted to implement some basic damage calculations from Pokemon using Python so that I could show what I've learned in a project that would actually interest me. 

This project implements damage calculations from generations one and three using formulas obtained from Bulbagarden. In order to simplify the user experience (because that's less important than the underlying functionality!), I assumed 0 EVs, IVs, and the like. 

This implementation focuses on: 
- Implementing the different generations of pokemon using basic inheritance for shared attributes
- Where applicable, leveraging writing functions that either work with the base class (ad-hoc polymorphism isn't really a thing in Python, sadly)
- Using custom data types (Move, Type) to make designing everything smoother and easier to follow
- Being (relatively) easy to expand with new generations or functionality; it should be pretty easy to allow for more knobs and dials on the user's end for things like level and EVs/IVs

The current form is more of a proof-of-concept, although the structure of the classes would allow for expansion of the move/pokemon roster (maybe using JSON, which shouldn't be hard)

This is more or less just a basic object-oriented design example
