from streamlit.components.v1 import html

def render_gridstack(windows_html):
    html(f"""
        <link href="https://cdn.jsdelivr.net/npm/gridstack@8.2.1/dist/gridstack.min.css" rel="stylesheet" />
        <script src="https://cdn.jsdelivr.net/npm/gridstack@8.2.1/dist/gridstack-h5.js"></script>

        <style>
            .grid-stack {{
                background: #f8f9fa;
            }}
            .grid-stack-item-content {{
                background-color: white;
                border-radius: 8px;
                padding: 10px;
                box-shadow: 0 2px 8px rgba(0,0,0,0.1);
                overflow: auto;
                height: 100%;
            }}
        </style>

        <div class="grid-stack">
            {windows_html}
        </div>

        <script>
            const grid = GridStack.init({{
                column: 3,
                cellHeight: 150,
                float: true,
                margin: 10,
                resizable: {{
                    handles: 'all'
                }},
                draggable: {{
                    handle: '.grid-stack-item-content'
                }}
            }});
        </script>
    """, height=900)