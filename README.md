# Task 1
The following awk command checks if the user has a shell to know if it is able to login and then show the shell and username of each user:
awk -F '[:]' '$7 != "/bin/false" && $7 != "/usr/sbin/nologin" {print $7 " " $1}' /etc/passwd
# Task 2
Run docker-compose build and docker-compose up to start the webapp in port 8000
###### Example: http://127.0.0.1:8000/fib/1/3
The Redis cache is exposed in port 6378 and the PostgreSQL DB is exposed in port 5434.  
The file simple_benchmark.py (need to run pip install redis first) runs some simple benchmarks and there is a conclusion in a comment at the end of the file.
