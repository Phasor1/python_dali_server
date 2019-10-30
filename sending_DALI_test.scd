s.boot;

x = NetAddr("192.168.1.46", 15200);

x.sendMsg("/Raffaello/Lights/GroupMessage", 0, 0);

x.sendMsg("/Raffaello/Lights/GroupMessage", 0, 1);

x.sendMsg("/Raffaello/Lights/Broadcast", 0);
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