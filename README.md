Kata Tennis
===========

### Description
En esta kata, nos centraremos únicamente en el sistema de puntuaciones del tennis. El sistema de puntuaciones del tennis es del estilo "back and forth", que presenta un tipo distinto de puntuaciones de otras katas como podría ser la Kata Bownling.

Para simplificar la kata, sólo se jugará un set del partido. Una vez terminado, habrá un ganador.
Normas del tennis
Básicas
En el juego del tennis, un jugador comienza con puntación 0. Los puntos se ganan en la siguiente secuencia: 0 -> 15 -> 30 -> 40

Si un jugador consigue 40 y puntua de nuevo, el jugador gana el juego, siempre que el otro jugador no tenga 40 puntos en ese momento. Si los dos jugadores tienen al mismo tiempo 40 puntos, a esto se llama "iguales" (deuce en inglés)

Iguales
Puntuar durante iguales, da al jugador "ventaja". Si el otro jugador puntua en ese momento, la puntuación vuelve a iguales.

Si un jugador tiene "ventaja" y puntua de nuevo, el jugador gana el juego.
Requerimientos
Escribe un programa para manejar cada uno de los siguientes requerimientos de puntuación de dos jugadores del juego de tennis.

 - Los jugadores deben poder ganar puntos.
 - El juego debe terminar con un ganador.
 - Debes de manejar la casuística de "iguales"
 - Después de terminar el juego, debe determinarse quién es el ganador.
 - Debe ser posible obtener la puntuación de cualquier de los jugadores en cualquier momento del partido.


### English description
This Kata is about implementing a simple tennis game. It is based on Wii tennis, where they have simplified tennis, so each set is one game. 

The scoring system is rather simple:

 - Each player can have either of these points in one game 0 15 30 40
 - If you have 40 and you win the ball you win the game, however there are special rules.
 - If both have 40 the players are deuce. a. If the game is in deuce, the winner of a ball will have advantage and game ball. b. If the player with advantage wins the ball he wins the game c. If the player without advantage wins they are back at deuce. 

### Alternate description of the rules per [Wikipedia](http://en.wikipedia.org/wiki/Tennis#Scoring):

 - A game is won by the first player to have won at least four points in total and at least two points more than the opponent.
 - The running score of each game is described in a manner peculiar to tennis: scores from zero to three points are described as "love", "fifteen", "thirty", and "forty" respectively.
 - If at least three points have been scored by each player, and the scores are equal, the score is "deuce".
 - If at least three points have been scored by each side and a player has one more point than his opponent, the score of the game is "advantage" for the player in the lead.

### Sources
- http://codingdojo.org/cgi-bin/index.pl?KataTennis
- http://craftsmanship.sv.cmu.edu/katas/tennis-game-kata

### Kata Tennis step by step. Python Sevilla 30/11/2012
http://es.slideshare.net/Javier_J/kata-tennis-paso-a-paso

[TDD](http://en.wikipedia.org/wiki/Test-driven_development)
===
- http://css.dzone.com/articles/tdd-python-5-minutes
- https://github.com/nestorsalceda/pycones2014

### Restricciones
 - Haz lo más simple que pueda funcionar
 - Escribe el mejor código que puedas
 - No hagas más de lo que pide la funcionalidad
 - No introduzcas infraestructura si la funcionalidad no lo pide explícitamente
 - No dependas de librerías si la funcionalidad no lo pide explícitamente

### Flujo
 - Evalua el impacto de cada funcionalidad
 - Realiza los cambios que necesites para que la funcionalidad sea facil de introducir
 - Introduce la funcionalidad


About running this code
=======================

### Testing
To run the test suite you need to install some dependencies. I am using [Mamba ](http://nestorsalceda.github.io/mamba/) as TDD suite

    $ virtualenv env
    $ source env/bin/activate
    $ pip install -r requirements.txt

### Run the game

    $ python 

Solutions
=========
- https://github.com/quiqueporta/kata_tenis
- https://github.com/malotor/tennis_kata
- https://github.com/giorgiosironi/python-tdd-tutorial
