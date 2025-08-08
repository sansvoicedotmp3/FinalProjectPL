# Welcome to my Pokemon Damage Simulator!

This project is for my Programming Languages class. I wanted to implement some basic damage calculations from Pokemon using Python so that I could show what I've learned in a project that would actually interest me. 

This project implements damage calculations from generations one and three using formulas obtained from Bulbagarden. In order to simplify the user experience (because that's less important than the underlying functionality!), I assumed 0 EVs, IVs, and the like. 

This implementation focuses on: 
- Implementing the different generations of pokemon using basic inheritance for shared attributes
- Having functionality stored in the class (real stat functions) where appropriate
- Using custom data types (Move, Type) to make designing everything smoother and easier to follow
- Being (relatively) easy to expand with new generations and/or functionality; it should be pretty easy to allow for more knobs and dials on the user's end for things like level and EVs/IVs

The current form is more of a proof-of-concept, although the structure of the classes would allow for expansion of the move/pokemon roster (maybe using JSON, which shouldn't be hard)

# Stylistic / Syntax information

I used Python for this project because I am familiar with it, and trust myself to write something of decent scale with it. However, there are some language design features that I had to work around when using this, as opposed to something like C++. 

I made the choice to use a lot of type hints (`type: str`, for example). Python's dynamic typing can be a strength, but for writing readable code, especially for something like this where not everyone will inherently understand what datatype a Pokemon type would be, type hints can be a big help. These also help me maintain consistency and use my code editor more efficiently. 

As far as I'm aware, variables that are `protected` in Python are more or less just "protected" based on the honors system, like how type hints are just that, hints. I chose to use this for some of my stat variables more so just to show that I understand the concept, but if I wanted a more robust implementation I could have made everything `private` and actually made a bunch of getters and setters. For the sake of this project, which is basically a calculator for a single user, protecting data like this seems unncecessary. Accessing base stats after creation isn't really something you'd have to do, anyway, so whatever. 

`GenericPokemon` could have been more fleshed out with some abstract class stuff, but given how the child classes actually function in regards to returning damage numbers for calculations, having a bunch of abstract methods for `GenericPokemon` would have cluttered the file.

> Why use inheritance at all?

What shared data there is between the different children can justify the use of inheritance, although beyond that it's not really used in the simulator implementation. I was going to use the `GenericPokemon` class as an argument for a function to get HP, because I realized I could fit that in there, but I ended up moving all of those functions into the child classes themselves, so it was no longer necessary. You can still see that code, though, in the simulator file.

# Justification

> So, how is this for a final project?

Honestly, I'll have to see how this is graded. I haven't compared my work to anyone else's, and I worked alone. Having read the guidance on the project provided, I think this implementation, although bare-bones in certain areas, is functional enough. It has the purely essential functionality of storing Pokemon base stats using some basic object-oriented design patterns, and then using those in calculations for damage.

# Usage:

It's really simple! Just download both files, have them in the same directory, and run `simulator.py` using Python! I used Python 3.12!
