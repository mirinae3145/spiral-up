# Guidance placement

This reference covers dividing guidance between skills, a user's own instructions, and project documents.
Use it when a change adds, revises, or moves guidance that could belong in more than one of them.

## Scope of each source

A skill is a reusable package shared with the users it is meant for, whether openly or within a group such as a team.
Fill it mainly with guidance that helps most of those users in the situations the skill defines.

Place each piece of guidance by the scope in which it holds:

- **Skills**: Judgments and procedures that hold for the skill's intended users in general.
- **User instructions**: A user's preferences, environment integration, and choices of when and how to use particular skills.
- **Project documents**: Decisions that belong to one project or repository, kept in its governing documents or templates.

## Direction of reference

A user's instructions may name a skill and override part of it.
Keep such overrides within what the skill safely allows where possible.

A skill's body is its entry document and the references agents read.
It names neither a user's instructions nor other specific skills, and does not override them.
When another area of guidance would help, recommend the area instead of a skill, as in "use together with scientific-writing guidance".

A repository README may name skills that can fill a recommended area as non-normative examples for the people who choose and install skills.
This exception holds only under all of the following conditions:

- **Location**: The README sits at the repository root, outside the skill folder.
- **No links from the body**: The skill body does not link to those examples.
- **Form**: The README states the recommended area first, gives two or more alternatives where possible, and links each repository.

## Moving guidance

When a user's instructions are generalized into a skill, narrow those instructions in the same change to what they still need.
When a skill comes to cover decisions that an instruction supplement makes, reassess the supplement and remove the overlap.
