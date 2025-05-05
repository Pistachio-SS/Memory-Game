# Memory-Game

The	game	will	display	a	square	grid,	with	the	columns	
labeled	with	letters,	and	the	rows	with	numbers.	
Elements	within	the	grid	will	be	associated	with	pairs	
of integers	(a	pair	of	0’s,	and	pair	or	1’s,	a	pair	of	2’s,	
etc.).	Initially,	we	will	not	be	able	to	see	any	of	the	
numbers,	as	they	will	be	hidden	by	‘X’	symbols.	Your	job	
as	a	player	is	to	find	the	hidden	pairs	in	as	few	guesses	
as	possible.	A	simple	menu	will	allow	you	to	interact	
with	the	game.

So	let’s	look	at	an	example.	The	image	to	the	right	
displays	the	game	interface	when	using	a	4x4	grid.	 You	
will	note	the	following:

• The	title	“Brain	Buster”	is	displayed	first.
• Next, we	have	the	grid.	Column	names use	
letters	(A	to	D	in	this	case),	while	rows	are	
labeled	with	numbers	(0	to	3	in	this	case).
• Any	individual	cell	in	the	grid	is	identified	by	a	
letter/number	combination	(e.g.,	A0,	B2).
• When	the	game	begins,	all	cells	display	an	X	(i.e.,	the	number	in	the	cell	is	‘hidden’).
• Below	the	grid	is	a	simple	menu	that	allows	you	to	play	the	game.	
• The	game	title,	grid,	and	menu	will	be	displayed	at	all	times.

Before	we	go	any	further,	let’s	look	at	the	pattern	of	numbers	that	are	actually	hidden	behind	the	X	
symbols.	

You	will	notice	that Menu	Option	3	is	entitled	“I	give	up	– reveal	the	grid”.	In	short,	this	ends	the	
game	and	displays	all	hidden	numbers.	So	if	we	select	that	option,	we	might	see	a	grid	display	that	
looks	like	the	image below.

Note	that	a	4	x	4	grid	has	16	cells	in	total.	As	such,	it	will	hold	8	
pairs	of	integers	(from	a	pair	of	0’s	up	to	a	pair	of	7’s).	In	contrast,	a	
6	x	6	grid	has	36	cells	and	therefore	18	pairs	of	integers	(from	0’s	
up	to	17’s).	

So	when	a	new	game	is	started,	the	grid	must	be	initialized	with	a	
new	set	of	pairs,	which	should	be	randomly	distributed	throughout	
the	grid.	To	demonstrate	this	feature,	we	can	use	Menu	Option	4	to	
start	a	new	game,	and	then	use	Menu	Option	3	to	reveal	the	new	
distribution.	

If	we	do	that,	we	might	see	the	set	of	numbers shown	in	the	image	
on	the	left. Note	that	we	again	have	8	pairs	of	integers	but	the	
values	are	distributed	in	a	completed	different	way.	This,	of	course,	
is	important	since	the	player must	not	be	able	to	simply	memorize	
a	fixed	pattern.	

Okay,	so	that’s	what	the	numbers	would	look	like.	So	back	to	the	
game	itself.	Again,	when	we	start	a	new	game,	all	we	see	is	a	grid	of	
X	symbols.	Our	job	is	to	find	the	pairs.	We	will	do	this	primarily	by	
selecting	Menu	Option	1,	which	will	allow	us	to	specify	a	pair	of	cells	to	test.	When	we	do	this,	we	
will	be	prompted	to	enter	the	first	cell	(using	the	letter/number	format)	and	then	the	second	cell	
(i.e.,	there	will	be	two	separate	input	prompts,	one	for	each	cell).	So	the	two	input	prompts	will	
appear	below	the	menu	and	might	look	like	this:

Note	that	column	letters may	be	given	either	as	upper	case	or	lower	case	(e.g.,	A	or	a).	In	any	case,	
once	this	selection	is	made,	the	contents	of	the	two	cells	will	be	revealed	(i.e.,	the	two	X’s	will	be	
replaced	by	the	integers associated	with	each	of	the	two	cells.	Early	in	the	game,	it	is	likely	that	your	
pair	will	not	match,	as	depicted	by	the	figure	below (A0	=	7,	B0	=	0).	In	this	case,	the	two	numbers	
will	remain	visible	for	2	seconds,	at	which	point	they	will	be	replaced	by	X’s	again.		As	a	player,	
your	job	is	to	try	to	remember	the	contents	of	these	cells	as	
you	uncover	other	cells	in	the	grid, so	that	you	can	eventually	
match	them	with	the	proper	cell.

Of	course,	if	the	two	cells	match,	then	the	numbers	will	
remain	visible	and	the	player	continues	to	search	for	other	
pairs.	

It	is	also	possible	for	a	player	to	manually	turn	cells	over	if	
they	want	to	solve	the	game	a	little	more	quickly.	To	do	so,	
they	will	select	Menu	Option	2.	In	this	case,	they	will	be	
prompted	to	enter	the	coordinates	for	a	single	cell.	The	associated	X	will	be	immediately	replaced	
by	the	number	in	that	cell.	

So	that’s	the	basic	idea.	Using	Menu	Options	1	and	2	(but	mostly	Option	1),	the	player	will	work	
through	the	grid	until	she/he	has	uncovered	all	of	the	pairs	in	the	grid.	At	that	point	the	game	will	
indicate	that	the	player	has	won	and	will	provide	a	score.	

What	is	this	score? In	short,	it	is	a	number	between	0	and	100	(higher	is	better)	that	represents	
how	quickly	the	player	was	able	to	find	all	pairs.	Basically,	the	score	reflects	the	number	of	guesses	
actually	taken	versus	the	minimum	number	actually	required.	So,	for	example,	the	minimum	
number	of	guesses	for	a	4	x	4	grid	would	be	8 (one	guess	for	each	valid	pair).	If	the	player	actually
uses	just	8	guesses	(VERY	unlikely),	they	will	get	a	score	of	100.	The	score	itself	is	a	very	simple	
calculation,	and	is computed	as	follows:

Score = (minimum_possible_guesses / actual_guesses) * 100
That’s	it	– the	closer	your	actual	guess	count	is	to	the	minimum	possible	number	of	guesses,	the	
closer	your	score	will	be	to	100.	
Note:	Using	Option	2	counts	as	two	guesses,	so	using	it	a	lot	will	produce	a	very	low	score.

The	figure	below	illustrates	the	display	when	the	player	wins.
In	this	case,	the	player	has	solved	the	
puzzle	but	has	done	so	in	4	guesses,	which	
is	twice	as	many	as	the	minimum	required	
for	a	2	x	2	grid.	So	her	score	is	50.0.	
Important:	If	a	player	solves	the	puzzle	
and	has	done	so	by	making	at	least	one	
valid	guess,	then	the	score	will	always be
greater	than 0.	

So	how	does	a	player	actually	get	a	score	
of	0?	Using	the	example	above,	it	would	be	
possible	to	use	Menu	Option	2	to	
manually	uncover	each	of	the	four	cells,	
without	ever	making	a	single	guess.	

In	this	
case,	the	victory	message	would	be	replaced	by	the	following	text:
In	practice, the	game	may	be	played	with	either	a	2x2	grid,	a	4x4	grid,	or	a	6x6	grid.	The	size	of	the	
grid	will	be	passed	as	a	command	line	argument	when	the	program	is	run	(i.e.,	either	2,	4,	or	6).
One	last	thing	that	has	to	be	mentioned	is	that	the	program	must	have	basic	error	checking.	
Otherwise,	the	program	will	fail	constantly,	as	the	player	accidentally	inputs	a	bad	selection.	The	
error	checking	includes:

1. Check	the	command	line	argument to	make	sure	that	a	2,	4,	or	6	has	been	specified.	The	
program	can	be	stopped	immediately	if	the	grid	size	is	invalid.

2. Check	the	menu	option	selections.	It	must	be	a	number	between	1	and	5.	If	a	bad	selection	
has	been	made,	the	player	must	be	informed	and	asked	to	enter	the	option	again	(the	
program	should	NOT	just	stop).

3. The	cell	coordinates	must	be	verified	to	ensure	that	the	column (a letter)	and	the	row	(the	
number)	are	valid	for	this	grid.	If	not,	the	player	should	be	informed	and	asked	to	enter	the	
cell(s)	again.	The	image	below	illustrates	user	feedback	when	invalid	entries	are	made.	Note	
as	well	that	the	player	should	not	be	able	to	enter	the	same	cell	twice	when	making	a	guess	
(e.g.,	a0	and	a0).	This	will	make	things	easier	for	you.
So	that’s	it.	The	game	is	not	hard	to	describe	and	is	fairly	simple	in	its	logic.	There	is just	a	set	of	
small	steps	that	must	be	properly	coordinated	so	that	the	game	ru
