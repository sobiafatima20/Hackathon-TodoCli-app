# Research Notes: Intermediate Level – Organization & Usability

## Decision: Task Priority Representation
**Rationale**: Using string values ("high", "medium", "low") for priority levels as specified in the feature requirements. This approach is simple and readable for CLI users.
**Alternatives considered**: Enum class, integer values (1-3), single character codes (H/M/L)

## Decision: Tag Storage Implementation
**Rationale**: Using a list of strings for tags to allow multiple tags per task and maintain simplicity. This aligns with the requirement for zero or more tags per task.
**Alternatives considered**: Comma-separated string, set data structure, dictionary with metadata

## Decision: Search Algorithm
**Rationale**: Implementing case-insensitive substring matching across title, description, and tags using Python's built-in string methods. This provides good performance for the expected task volume (up to 100 tasks).
**Alternatives considered**: Regular expressions, fuzzy matching, external search libraries (not allowed per constitution)

## Decision: CLI Command Structure
**Rationale**: Adding new commands for search/filter/sort while maintaining backward compatibility with existing commands. Using intuitive command names that match the feature requirements.
**Alternatives considered**: Adding flags to existing commands, creating subcommands

## Decision: Filter Implementation
**Rationale**: Implementing filter as a separate method in TaskManager that can accept multiple criteria and combine them. This maintains separation of concerns and allows for future expansion.
**Alternatives considered**: Multiple separate filter methods, inline filtering in CLI layer

## Decision: Sort Implementation
**Rationale**: Implementing temporary sorting that doesn't modify the original task storage order, as specified in requirements. Using Python's built-in sorted() function with custom key functions.
**Alternatives considered**: Maintaining separate sorted views, in-place sorting (rejected per requirements)