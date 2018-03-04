# TNS
## the-elite Notification System

## Setup

### Database

- Install and configure latest PostgreSQL (e.g 9.6.5)
- Create a user and a database, ex:

```
# create the user, fill in the info
createuser -P --interactive

# create user with the owner as whatever user you created above
createdb -O <user>

# test it out
psql -h localhost <user> -U <pass>
```

- Configure it in config/tns.yml