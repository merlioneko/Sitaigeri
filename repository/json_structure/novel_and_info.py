story_json = {
    "type": "object",
    "properties": {
    "story": {
        "type": "string",
        "description": "The complete story of the novel, including all scenes and character interactions. Don't include any additional information or context, just the story itself."
    },
    "info": {
        "type": "string",
        "description": "Additional information about the novel. Don't include any story content, just supplementary details."
    }
    },
    "required": [
    "story",
    "info"
    ]
}