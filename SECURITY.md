# Security

## Project status

This application was developed in 2023 as a team project for educational
purposes. It is not maintained for production use.

## Reporting a problem

Please do not open a public issue. Use
[private vulnerability reporting](https://github.com/elenasorrentino10/Project_Opinion_Vote/security/advisories/new)
and describe the problem and how to reproduce it. Response times are not guaranteed.

## Known limitations

- Any user of the application can clear the whole Redis database.
- Connection details for Redis must be set as environment variables and never
  committed. Use a dedicated, non-production Redis instance.
- Credentials found in old commits or branches of this repository have been
  disabled and are no longer valid.
