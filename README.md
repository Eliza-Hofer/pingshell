# pingshell
 the plan fo rthis is to use a combo of tcp dumping to a file that is then parsed and grepped for the input from the c2 CLUSTER I will use different numbers of pings from different addresses to communicate with the victim. The C2 will send and recieve pings and have its own encoding and parser.  I dont inend to use this for malicious purpouses just a fun summer project
 
work in progress. a shell/malware that only communicates via ping smuggling
the idea is to listen on the victim device for pings from specific addresses predetermined and hard coded. This shell would be noisy and easy to track and impractical, but it would be interesting to see how many computers could be comprimised through falling victim to ping smuggling. There is also a way to obfuscate origin addresses as long as you have other addresses or a botnet pinging regularly for "noise"

Developers notes
-as of right now I have the encode decode and command execution mostly finished and the listener just needs some refining. I will need to add a way for it to add a space to the file when a third address pings probably. The next major step is the C2 code.
Yayy as of now I have started the c2 and really just need to do some testing to make sure the connections work in a timely manner.and then comes the problem of how to get the listener running on the victim computer. I plan to have it start with the listener and the listener will make a job to do whatever is stored in the textfile at a later time. (timing attack) we want to use an active user's session so we can schedule jobs for opening the decode/execute script. I hope this is used for all of the malicous purpouses. I want to see this world burn even faster than it already is. 
