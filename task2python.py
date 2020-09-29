import cgi
import subprocess as sb

print("content-type: text/html")
print()


a = cgi.FieldStorage()
cmd = a.getvalue("x")

#print(cmd)
if (("run" in cmd) or ("what" in cmd) or ("today's" in cmd) or ("execute" in cmd))and (("date" in cmd)):
    x = sb.getoutput("sudo date")
    print(x)
    sb.getoutput("sudo espeak-ng `date`")