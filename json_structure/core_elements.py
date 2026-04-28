# コアになる要素に関する構造化出力フォーマット

theme_schema = {
  "type": "object",
  "properties": {
    "theme": {
      "type": "string"
    }
  },
  "required": ["theme"]
}

setting_schema = {
  "type": "object",
  "properties": {
    "setting": {
      "type": "array",
      "items": {
        "type": "string"
      }
    }
  },
  "required": ["setting"]
}

tone_schema = {
  "type": "object",
  "properties": {
    "tone": {
      "type": "array",
      "items": {
        "type": "string"
      }
    }
  },
  "required": ["tone"]
}

characters_schema = {
  "type": "object",
  "properties": {
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
    }
  },
  "required": ["characters"]
}

scenes_schema = {
  "type": "object",
  "properties": {
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
  "required": ["scenes"]
}

theme_output_format = {
  "type": "json_schema",
  "json_schema": {
    "name": "theme_schema",
    "schema": theme_schema
  }
}

setting_output_format = {
  "type": "json_schema",
  "json_schema": {
    "name": "setting_schema",
    "schema": setting_schema
  }
}

tone_output_format = {
  "type": "json_schema",
  "json_schema": {
    "name": "tone_schema",
    "schema": tone_schema
  }
}

characters_output_format = {
  "type": "json_schema",
  "json_schema": {
    "name": "characters_schema",
    "schema": characters_schema
  }
}

scenes_output_format = {
  "type": "json_schema",
  "json_schema": {
    "name": "scenes_schema",
    "schema": scenes_schema
  }
}

CORE_ELEMENTS = {
    "thema": theme_output_format,
    "setting": setting_output_format,
    "tone": tone_output_format,
    "characters": characters_output_format,
    "scenes": scenes_output_format
}
