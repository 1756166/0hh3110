# 0h h3110

A summer programmer &amp; STEM endeavor

The [0h h1 game][ohhi] ([github][ohhi-github]) is a logic game to place two color pieces on a board according to a set of rules.  The 0h h3110 summer project develops an automated gaming platform to simulate out large-scale versions of the game, amongst other aspects.

![0h h1 board as shown on their website](/docs/0hh1-screenshot-small.png?raw=true)

0h h3110 is developed as a client-server model, so that multiple clients can place the color pieces on the board.  

### Design
A server will host the game and accept TCP client connections.  Multiple clients will connect and the servers and clients will communicate using [protobufs][protobuf].  Each client may only make one move at a time, and for each move the server will retransmit the updated board to all clients.

To begin the development, clients will only be programmed to look for one of the logic rules.  Clients will be run on multiple computers (say, the jetsons and laptops) to see how fast a board can be solved.

Large-scale boards will be simulated many times to understand how performance varies with different types of clients, for higher-dimensional boards (3D, 4D, and higher).  Additional game rules can be applied.

### Key concepts to explore

* large-scale simulations and the Monte Carlo method
* efficient network communication
* high-speed array indexing for multi-dimensional arrays
* CPU and GPU programming in python (using [theano][theano]), [torch][torch] and other languages

### Components

* Python server with HTTP front end for clients to connect
    * automatically generate new board starts
    * Data logging/storage for the game moves to replay and understand game progression
* Web browser visualization for the current board or for multiple game runs
    * AJAX enabled
    * could try protobuf.js
* Clients that implement game rules and provide the server with new moves
    * written using a variety of languages and libraries



[ohhi]: http://0hh1.com/
[ohhi-github]: https://github.com/Q42/0hh1

[protobuf]: https://developers.google.com/protocol-buffers/docs/overview
[theano]: http://deeplearning.net/software/theano/
[torch]: http://torch.ch/

