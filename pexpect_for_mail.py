import pexpect
import sys
m = pexpect.spawn('python gmail_sample.py')
m.logfile_read = sys.stdout
m.expect("Username:")
m.sendline("ramarao4507@gmail.com")
m.expect("Password:")
m.sendline("Ramarao1@")
m.expect("To address :")
m.sendline("surajdubey302.sd@gmail.com")
m.expect("Subject :")
m.sendline("Hai")
m.expect("Enter the content. Your last line should be as 'end'")
m.sendline("hello")
m.sendline("end")
m.expect("test has been send to surajdubey302.sd@gmail.com")
m.close()
