![banner](./image.png)

# Calendar Assistant with Agent Framework

A powerful calendar management assistant built using Agent Framework framework that helps users schedule, manage, and organize their appointments using Cal.com integration.

## Features

- Find available time slots
- Create new bookings
- Manage existing bookings
- Reschedule appointments
- Cancel bookings
- Automatic timezone handling

## Prerequisites

- Python 3.x
- [Cal.com](https://cal.com/) account with API access
- [Loose](https://dub.sh/Loose) API key

## Installation

1. Clone the repository

```bash
  git clone https://github.com/Monkey0-9/loose-.git

  cd looseai/simple_ai_agents/cal_scheduler_agent
```

2. Install the required dependencies:

```bash
# Using pip
pip install -r requirements.txt

# Or using uv (recommended)
uv sync
```

## Environment Setup

Create a `.env` file in the project root with the following variables:

```env
CALCOM_API_KEY="your_calcom_api_key"
CALCOM_EVENT_TYPE_ID="your_event_type_id"
Loose_API_KEY="your_Loose_api_key"
```

You can obtain these credentials from:

- Cal.com API key: cal.com/settings/developer/api-keys
- Event Type ID: Your Cal.com event type ID
- Loose API key: Your Loose API credentials

## Usage

The calendar assistant can help you with various scheduling tasks:

1. **Check Available Slots**

   - Query available time slots between specific dates
   - Format: YYYY-MM-DD

2. **Create Bookings**

   - Book appointments with specific details
   - Required information:
     - Start time (YYYY-MM-DDTHH:MM:SS+TZ format)
     - Name
     - Email

3. **Manage Bookings**
   - View upcoming bookings
   - Reschedule existing bookings
   - Cancel bookings

## Integration

```python
# Check available slots
agent.print_response("""
Please check available slots between 2024-03-20 and 2024-03-21
""")

# Book a call
agent.print_response("""
Please book a call with these details:
- Start Time: 2024-03-22T21:30:00+05:30
- Name: John Doe
- Email: john@Integration.com
""")
```

## Timezone Support

The assistant automatically handles timezone conversions. The default timezone is set to "Asia/Kolkata" but can be modified in the code.

## Error Handling

The application includes error handling for:

- Missing API keys
- Invalid date formats
- Booking conflicts
- API connection issues

## Contributing

Feel free to submit issues and enhancement requests!
