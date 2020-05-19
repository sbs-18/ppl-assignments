:-initialization(main).
main :- write('AIRLINE MANAGEMENT SYSTEM').

place('Toronto',1,50,60).
place('London',2 ,75,80).
place('Barcelona',3,40,30).
place('Madrid',4,75,45).
place('Valenca',5,40,20).
place('Malaga',6,50,30).
place('Paris',7,50,60).
place('Toulouse',8,40,30).

code('Toronto',1).
code('London',2).
code('Barcelona',3).
code('Madrid',4).
code('Valenca',5).
code('Malaga',6).
code('Paris',7).
code('Toulouse',8).

airline('Iberia',1).
airline('Air Canada',2).
airline('United',3).

route(1,2,2,500,360).
route(1,2,3,650,420).
route(1,4,1,800,480).
route(1,4,2,900,480).
route(1,4,3,950,540).
route(2,3,1,220,240).
route(3,4,2,100,60).
route(3,4,1,120,65).
route(4,5,1,40,50).
route(4,6,1,50,60).
route(5,6,1,80,120).
route(7,8,3,35,120).

print_flightdetails(From,To,F,D,E) :- 
nl,write('Departing From :'),
write(From),
nl,write('Arriving At :'),
write(To),
nl,write('Airline :'),
write(F),
nl,write('Price :'),
write(D),
write('$'),
nl,write('Duration :'),
write(E),
write(' minutes').


flight_check(From,To) :-
code(From,A),
code(To,B),
route(A,B,C,D,E),
airline(F,C),
print_flightdetails(From,To,F,D,E).


flight(From,To):-
flight_check(From,To);flight_check(To,From).

airport(city,airporttax,minsecuritydelay) :-
nl,write('Getting details for all cities in database.............'),
place('Toronto',1 ,50 ,60),
nl,write('Toronto ,Tax:50$, Delay:60Mins'),
place('London',2 ,75 ,80),
nl,write('London , Tax:75$, Delay:80Mins'),
place('Barcelona',3 ,40 ,30),
nl,write('Barcelona, Tax:40$, Delay:30Mins'),
place('Madrid',4 ,75 ,45),
nl,write('Madrid , Tax:75$, Delay:45Mins'),
place('Valenca',5 ,40 ,20),
nl,write('Valenca , Tax:40$, Delay:20Mins'),
place('Malaga',6 ,50 ,30),
nl,write('Malaga , Tax:50$, Delay:30Mins'),
place('Paris',7,50 ,60),
nl,write('Paris , Tax:50$, Delay:60Mins'),
place('Toulouse',8 ,40 ,30),
nl,write('Toulouse , Tax:40$, Delay:30Mins').

check_price(A,B):-
A<B,
nl,write('Cheap').

cheap_price(From,To,Airline):-
code(From,A),
code(To,B),
airline(Airline,C),
check(A,B,C);check(B,A,C).

check(A,B,C):-
route(A,B,C,D,E),
check_price(D,400).

united_check:-
route(A,B,3,D,E),
route(A,B,2,D,E).