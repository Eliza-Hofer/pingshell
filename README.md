# pingshell
work in progress. a shell/malware that only communicates via ping smuggling
the idea is to listen on the victim device for pings from specific addresses predetermined and hard coded. This shell would be noisy and easy to track and impractical, but it would be interesting to see how many computers could be comprimised through falling victim to ping smuggling. There is also a way to obfuscate origin addresses as long as you have other addresses or a botnet pinging regularly for "noise"

Developers notes
-as of right now I have the encode decode and command execution mostly finished and the listener just needs some refining. I will need to add a way for it to add a space to the file when a third address pings probably. The next major step is the C2 code.
