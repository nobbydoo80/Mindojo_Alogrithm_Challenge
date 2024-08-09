import gspread
from oauth2client.service_account import ServiceAccountCredentials

def get_google_sheet():
    scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
    creds = ServiceAccountCredentials.from_json_keyfile_name('credentials.json', scope)
    client = gspread.authorize(creds)
    sheet = client.open_by_url('https://docs.google.com/spreadsheets/d/1guE4DI4wQpBXPlXRKXVEeb3nH84Phq6YqgYK9M4NUT0/edit?gid=0#gid=0')
    return sheet

def count_cells_with_flow_to_oceans(matrix):
    if not matrix or not matrix[0]:
        return 0

    rows, cols = len(matrix), len(matrix[0])
    
    def bfs(starts):
        queue = starts
        reachable = set(starts)
        while queue:
            new_queue = []
            for r, c in queue:
                for nr, nc in ((r+1, c), (r-1, c), (r, c+1), (r, c-1)):
                    if 0 <= nr < rows and 0 <= nc < cols and (nr, nc) not in reachable and matrix[nr][nc] >= matrix[r][c]:
                        reachable.add((nr, nc))
                        new_queue.append((nr, nc))
            queue = new_queue
        return reachable

    # Cells that flow to the northwest edges
    northwest_starts = [(0, c) for c in range(cols)] + [(r, 0) for r in range(1, rows)]
    northwest_reachable = bfs(northwest_starts)

    # Cells that flow to the southeast edges
    southeast_starts = [(rows-1, c) for c in range(cols)] + [(r, cols-1) for r in range(rows-1)]
    southeast_reachable = bfs(southeast_starts)

    # Intersection of both reachabilities
    result = northwest_reachable & southeast_reachable
    
    return len(result)
