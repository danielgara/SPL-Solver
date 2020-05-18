# REST API
---

This project exposes a Flask server with a REST API to make easier to integrate multiple Software Product Line solvers into the Variamos project. This API allows to integrate CNF and XCSP to any web project.

## Feature Model
---

The feature model is described as a JSON blob, the idea is to send this blob structure each time a validation of the Feature Model is required. This structure is described by a JSON schema that validates the proper structure of the JSON before transforming the data into the solvers specific language.

**Example Feature Model JSON**

![alt text](./jupyter/images/feature_model_example.png "Example Feature Model")

```javascript
{
  "name": "Mobile Phone Feature Model",
  "author": "Paolo Vavassori",
  "description": "Example of a Feature Model",
  "features": [
    {
      "id": 1,
      "name": "Mobile Phone",
      "constraints": [
        {
          "constraint_type": "root"
        },
        {
          "constraint_type": "mandatory",
          "destination": 2
        },
        {
          "constraint_type": "optional",
          "destination": 3
        },
        {
          "constraint_type": "mandatory",
          "destination": 4
        },
        {
          "constraint_type": "optional",
          "destination": 5
        }
      ]
    },
    {
      "id": 2,
      "name": "Calls"
    },
    {
      "id": 3,
      "name": "GPS",
      "constraints": [
        {
          "constraint_type": "excludes",
          "destination": 6
        }
      ]
    },
    {
      "id": 4,
      "name": "Screen",
      "constraints": [
        {
          "constraint_type": "group_cardinality",
          "low_threshold": 1,
          "high_threshold": 3,
          "destination": [
            6,
            7,
            8
          ]
        }
      ]
    },
    {
      "id": 5,
      "name": "Media",
      "constraints": [
        {
          "constraint_type": "or",
          "destination": [
            9,
            10
          ]
        }
      ]
    },
    {
      "id": 6,
      "name": "Basic",
      "constraints": [
        {
          "constraint_type": "excludes",
          "destination": 3
        }
      ]
    },
    {
      "id": 7,
      "name": "Colour"
    },
    {
      "id": 8,
      "name": "High Resolution"
    },
    {
      "id": 9,
      "name": "Camera",
      "constraints": [
        {
          "constraint_type": "requires",
          "destination": 8
        }
      ]
    },
    {
      "id": 10,
      "name": "MP3"
    }
  ]
}
```

### Feature Model is Empty -- CNF
---

* **URL**

  <HOST>/feature-model/cnf/is-empty
  
* **METHOD**

  `POST`
  
* **URL Params**

  **required**
  `id=[feature-model]`
  
### Is Real Product Line -- CNF
---

* **URL**

  <HOST>/feature-model/cnf/is-real
  
* **METHOD**

  `POST`
  
* **URL Params**

  **required**
  `id=[feature-model]`
  
### Get Dead Features -- CNF
---

* **URL**

  <HOST>/feature-model/cnf/dead-features
  
* **METHOD**

  `POST`
  
* **URL Params**

  **required**
  `id=[feature-model]`

### Get Fake Optional -- CNF
---

* **URL**

  <HOST>/feature-model/cnf/fake-optionals
  
* **METHOD**

  `POST`
  
* **URL Params**

  **required**
  `id=[feature-model]` 
