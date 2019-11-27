s.boot;

x = NetAddr("192.168.1.46", 15200);

x.sendMsg("/Raffaello/Lights/GroupMessage", 0, 0);

x.sendMsg("/Raffaello/Lights/GroupMessage", 0, 1);

x.sendMsg("/Raffaello/Lights/Broadcast", 0);

x.sendMsg("/Raffaello/Lights/lightValue", 0);
x.sendMsg("/Raffaello/Lights/lightValue", 1);
x.sendMsg("/Raffaello/Lights/lightValue", 2);
x.sendMsg("/Raffaello/Lights/lightValue", 3);
x.sendMsg("/Raffaello/Lights/lightValue", 4);
x.sendMsg("/Raffaello/Lights/lightValue", 5);
x.sendMsg("/Raffaello/Lights/lightValue", 6);
x.sendMsg("/Raffaello/Lights/lightValue", 7);
x.sendMsg("/Raffaello/Lights/lightValue", 8);
x.sendMsg("/Raffaello/Lights/lightValue", 9);
x.sendMsg("/Raffaello/Lights/lightValue", 10);
~me = true;
(
t = Task({
	inf.do{
		var msg = if(~me == true, {0}, {1}),
		time = 1 + 20.rand();
		postln(msg);
		x.sendMsg("/Raffaello/Lights/GroupMessage", 0, msg);
		~me = ~me.not;
		postln(time + "seconds");
		time.wait();
	}
});
)
t.start;
t.stop;