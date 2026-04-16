base_json = {
  "type": "object",
  "properties": {
    "theme": {
      "type": "string"
    },
    "setting": {
      "type": "array",
      "items": {
        "type": "string"
      }
    },
    "tone": {
      "type": "array",
      "items": {
        "type": "string"
      }
    },
    "characters": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "name": {
            "type": "string"
          },
          "role": {
            "type": "string"
          },
          "description": {
            "type": "string"
          }
        },
        "required": [
          "name",
          "role"
        ]
      }
    },
    "scenes": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "number": {
            "type": "integer"
          },
          "title": {
            "type": "string"
          },
          "tone": {
            "type": "array",
            "items": {
              "type": "string"
            }
          },
          "description": {
            "type": "string"
          }
        },
        "required": [
          "number",
          "title",
          "tone",
          "description"
        ]
      }
    }
  },
  "required": [
    "theme",
    "setting",
    "tone",
    "characters",
    "scenes"
  ]
}