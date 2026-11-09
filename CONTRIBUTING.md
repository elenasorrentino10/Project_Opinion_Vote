# Contributing

This is a 2023 educational project, so changes may not be reviewed quickly.

## Run the project

Follow the "Getting Started" section of the README. Use a local Redis instance,
for example the Docker command shown there.

## Run the tests

From the repository root:

```
python -m unittest discover tests
```

## Propose a change

1. For larger changes, open an issue first.
2. Create a branch from `main`.
3. Add or update tests when you change password handling.
4. Open a pull request explaining what changes and why.

## Project rules

- Never commit passwords, hosts or `.env` files.
- Do not use real personal data in examples or tests.

Contributions are distributed under the project's MIT license.
