CCFLAGS = -g3 -wall -o0

all: send_app

%.o:%.cc
	$(CXX) $(CCFLAGS) -c -o $@ $^

send_app: send_app.o
	$(CXX) -o $@ $^

clean: 
	rm -f *.o send_app





