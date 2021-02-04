# ACID Database Transactions

Source: https://www.youtube.com/watch?v=5Pia4UFuMKo

- consider we want make a db for a bank
- if we want to make a bank transfer, we need to ensure that either all queries and done successfully, or none of them are done at all
  - either there is a transfer, or there isnt a transfer
  - if we have something midway, we'll fail a withdraw and succeed a deposit, we dont want to give people free money...
- in databases, a transaction is an indivisible unit of work
- if we want to move rows from one table to another, we can use `INSERT INTO` and `DELETE`, packed together into one transaction, so that we dont generate or delete any data
- you can write specific stored procedures that can be called and run as one single database transaction
  - within producedures, you can have try catches, and can manually run `BEGIN`s, `COMMIT`s, and `ROLLBACK`s on transactions
  - ![example](https://i.imgur.com/i2ML3e1.png)
- SQL/transact-SQL allows a lot of control over transactions
  - you can have transactions within transactions, or have transactions roll back to a certain point within the transaction, etc..

## Acronym
- A: Atomic, transaction has to run successfully, or not at all
- C: Consistent, data must be in a consistent state before and after the transaction
- I: Isolated, the data cannot be changed by another user while a transaction is running
- D: Durable, the transaction should ensure that the data is persisted after its execution
