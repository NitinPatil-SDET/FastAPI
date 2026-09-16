# Pydantic: Data Validation and Schema Management

## Overview

Pydantic is a Python library used for **data validation**, **type enforcement**, and **data parsing**. It is widely used in frameworks such as **FastAPI**, configuration management using **YAML**, and **Data Science / Machine Learning pipelines**.

Pydantic helps ensure that incoming data conforms to a predefined schema, reducing runtime errors and improving data quality.

---

## Key Details

### Why Use Pydantic?

- Strong type checking and type hinting support.
- Automatic data validation.
- Automatic conversion of input data into appropriate Python types.
- Prevention of invalid data, such as negative ages or incorrectly formatted emails.
- Cleaner, safer, and more maintainable code.

### Pydantic Workflow

#### Step 1: Define a Pydantic Model

Create a Pydantic class that represents the ideal schema of the data.

#### Step 2: Instantiate the Model with Raw Data

Provide raw input data, usually in the form of a dictionary or JSON object.

Pydantic automatically:

- Validates the data.
- Converts compatible data types.
- Raises validation errors when data is invalid.

#### Step 3: Use the Validated Object

Benefits:

- Clean data
- Type-safe processing
- Logically valid inputs
- Reduced validation code

### Required, Optional, and Default Fields

#### Required Field

Field must be provided.

#### Optional Field

Field can be omitted.

#### Default Field

A default value is automatically assigned if no value is provided.

### Specialized Data Types

#### Email Validation

`EmailStr` ensures a valid email format.

#### URL Validation

`AnyUrl` ensures a valid URL format.

### Field-Based Validation

Use `Field()` to:

- Apply validation constraints.
- Add metadata.
- Define descriptions and examples.
- Improve API documentation.

Examples:

- `Field(gt=0)` → value must be greater than zero.
- `Field(max_length=5)` → restrict maximum length.

### Annotated Usage

Benefits:

- Cleaner code
- Reusable validation rules
- Better readability
- Improved type definitions

### Field Validators

Use `field_validator` for custom business logic or data transformations.

Examples:

- Convert names to uppercase.
- Remove extra spaces.
- Apply custom validation rules.

#### Validation Modes

##### Before Mode

Runs before type conversion and validation.

##### After Mode (Default)

Runs after standard validation.

### Model Validators

Use `model_validator` when validation depends on multiple fields or the complete model.

Examples:

- Password confirmation.
- Start date must be before end date.
- Cross-field business rules.

### Computed Fields

Computed fields:

- Do not require user input.
- Are generated from existing fields.
- Help maintain consistent derived values.

### Nested Pydantic Models

Advantages:

1. Better data organization.
2. Model reusability.
3. Improved readability.
4. Built-in validation.

### Model Serialization and Export

#### Convert Model to Dictionary

`model_dump()`

#### Convert Model to JSON

`model_dump_json()`

#### Include Specific Fields

`model_dump(include={})`

#### Exclude Specific Fields

`model_dump(exclude={})`

#### Exclude Unset Fields

`model_dump(exclude_unset=True)`

---

