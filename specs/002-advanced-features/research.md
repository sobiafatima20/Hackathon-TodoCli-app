# Research Notes: Advanced Level – Intelligent Features

## Technical Decisions

### 1. Recurrence Implementation Approach

**Decision**: Implement recurrence as a pattern-based system where completing a recurring task creates a new instance rather than rescheduling the same task.

**Rationale**: This approach maintains data integrity and allows for tracking of task completion history while still providing the recurrence functionality users need.

**Alternatives Considered**:
- Modifying due date of same task ID: Would lose completion history
- Creating separate recurrence scheduler: Would add complexity and require persistence

**Trade-offs**:
- ✅ Maintains completion history
- ✅ Simple implementation
- ❌ Creates multiple task entries in system

### 2. Due Date Storage Format

**Decision**: Use Python's datetime object for internal storage and display dates in YYYY-MM-DD format.

**Rationale**: datetime objects provide robust date manipulation capabilities while maintaining compatibility with Python's standard library.

**Alternatives Considered**:
- String storage: Would require custom parsing
- Unix timestamps: Less readable and harder to work with

**Trade-offs**:
- ✅ Standard Python datetime handling
- ✅ Easy date arithmetic
- ✅ Consistent formatting

### 3. Reminder System Implementation

**Decision**: Implement CLI-based reminders that display information when viewing tasks rather than background notifications.

**Rationale**: Aligns with the CLI-only requirement and avoids complexity of background processes.

**Alternatives Considered**:
- Background scheduler: Would require daemon processes
- System notifications: Would require external libraries

**Trade-offs**:
- ✅ No external dependencies
- ✅ Simple implementation
- ❌ Reminders only visible when using CLI

## Architecture Considerations

### 1. Backward Compatibility

**Approach**: Add new fields with default values to maintain compatibility with existing tasks.

**Implementation**: All new fields have sensible defaults (None, False, etc.) so existing tasks remain functional.

### 2. Performance Implications

**Consideration**: Due date and recurrence checks could impact performance with large numbers of tasks.

**Mitigation**: Use efficient datetime comparisons and limit operations to necessary checks only.

### 3. Data Integrity

**Consideration**: Recurrence chains could become complex to manage.

**Approach**: Use original_task_id to track recurrence lineage while keeping implementation simple.

## Implementation Patterns

### 1. Task Creation Pattern
- New tasks with recurrence settings create a "template" task
- When template is completed, a new instance is created with updated due date
- Template remains to continue the recurrence pattern

### 2. Date Comparison Pattern
- Use datetime.date() for date-only comparisons
- Compare against current date for overdue/upcoming checks
- Use timedelta for interval calculations

### 3. CLI Interaction Pattern
- Extend existing command flow with additional prompts
- Maintain consistent error handling and messaging
- Use same input validation patterns as existing commands

## Known Limitations

1. **No Background Processing**: Reminders only appear when actively using the CLI
2. **Memory-Only Storage**: Recurrence patterns are lost when application exits
3. **Simple Recurrence**: Only interval-based recurrence (no complex schedules like weekdays only)
4. **No Recurrence History**: Cannot track completion history of recurring tasks beyond individual instances

## Future Considerations

1. **Persistence**: If persistence is added later, recurrence patterns could be maintained across sessions
2. **Complex Scheduling**: More sophisticated recurrence patterns could be added in future versions
3. **Notification Options**: Different reminder display options could be implemented based on user feedback