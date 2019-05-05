CCFLAGS = -g3 -wall -o0

all: recv_app

%.o:%.cc
	$(CXX) $(CCFLAGS) -c -o $@ $^

recv_app: recv_app.o
	$(CXX) -o $@ $^

clean: 
	rm -f *.o recv_app





