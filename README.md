# Vote My Choice

This is a CLI (command-line interface) application written in Python that facilitates the process of voting on proposals by users. The application utilizes Redis as its database and focuses on efficiency. It allows users to perform various actions such as identifying themselves, submitting proposals, viewing proposals and voting on proposals.

## Features

- *Identify user*: Users can identify themselves before performing any actions in the application.
- *Insert proposal*: Users can submit proposals after identifying themselves. Duplicate proposals are not allowed. If a proposal is similar to one already present, the application will prompt the user to choose between voting for the existing proposal or inserting their proposal anyway if it differs from the existing one.
- *View proposals*: Users can view the list of proposals currently available, ordered by the number of votes.
- *Vote on a proposal*: Users can vote on proposals after identifying themselves. Each user can only vote once for a specific proposal.
- *Delete account*: Users can delete their account, but they need to identify themselves first.
- *Flush/Clear Redis database*: Users can clear the Redis database, removing all proposals and user information. This is mainly for "admin" use.

## Getting Started

1. To get started you need to clone the repository to your local machine, you can do it with the following command:

```
git clone https://github.com/elenasorrentino10/Project_Opinion_Vote.git
```

2. You then need to change to the cloned repository, you can do it with the following command:

```
cd Project_Opinion_Vote
```

3. To use this application, you need to have Python installed on your system. Additionally, ensure that the required libraries are installed by running the following command:

```
pip install -r requirements.txt
```

4. Once the dependencies are installed, you can execute the `main.py` file to start the application. First you need to enter into the "project" folder with the following command:

```
cd project
```
- Then you can run the main file:
```
python main.py
```

## Usage

1. Run the application by executing the `main.py` file.
2. The application will display a menu with several options.
3. Enter the number corresponding to the action you want to perform and press Enter.
4. Follow the instructions prompted by the application for each action.

## Example Usage

- Actions display
```
=== Vote my choice! ===
1. Identify user
2. Insert proposal
3. View proposals
4. Vote a proposal
5. Delete account
6. Flush/Clear Redis database
0. Exit/Quit
Enter your action (1-6): 2

You need to identify yourself before submitting a proposal!
```
- User identification
```
1. Identify user

Please enter your username: John
```
- Submitting proposals
```
2. Insert proposal

Enter the proposal description: Free snacks in the cafeteria
```
- Displaying all current proposals
```
3. View proposals

Current proposals:
1. Free snacks in the cafeteria (Alice): 1 votes
```
- Voting a proposal
```
4. Vote a proposal

Enter the proposal number you want to vote for: 1
```
- When not signed-in
```
4. Vote a proposal

You need to identify yourself before voting on a proposal!
```
- Account deletion
```
5. Delete account

Deleting your account...
```
- Clearing Database
```
6. Flush/Clear Redis database

Exiting the program...
```

## Note

This application was developed for educational purposes and may not be suitable for production environments.
