import json

style = """
<style>
    table {
        border: none;
        border-collapse: collapse;
    }
    td {
        width: 40px;
        height: 40px;
        text-align: center;
    }
    .b1 {
        background-color: #4A7BBA;
    }
    .b2 {
        background-color: #C174A8;
    }
    .b3 {
        background-color: #4DAFD0;
    }
    .b4 {
        background-color: #87BD56;
    }
    .b5 {
        background-color: #353289;
    }
    .b6 {
        background-color: #459FD7;
    }
    .b7 {
        background-color: #FCE84E;
    }
    .b8 {
        background-color: #4A4A59;
    }
    .b9 {
        background-color: #D93841;
    }
    .b10 {
        background-color: #E37C3A;
    }
    .b11 {
        background-color: #6A3C27;
    }
    .b12 {
        background-color: #79848B;
    }
    .bt {
        border-top: 5px solid #000000;
    }
    .bb {
        border-bottom: 5px solid #000000;
    }
    .bl {
        border-left: 5px solid #000000;
    }
    .br {
        border-right: 5px solid #000000;
    }
    .by {
        border-bottom: 1px dashed #AAAAAA;
    }
    .bx {
        border-left: 1px dashed #AAAAAA;
    }
    body {
        display: flex;
        flex-direction: column;
        align-items: center;
        font-family: Arial, sans-serif;
    }
    .container {
        width: 850px;
        margin-bottom: 20px;
    }
    #pieces {
        height: 90px;
        overflow-x: auto;
        white-space: nowrap;
        display: flex;
        justify-content: flex-start;
        align-items: center;
    }
    #pieces table {
        display: inline-block;
        width: 60px;
        margin: 5px;
    }
    .pieces-fieldset {
        border: 1px solid #ccc;
        padding: 20px;
        margin-bottom: 20px;
        width: 850px;
        height: 100px;
    }
    fieldset legend {
        font-size: 1.2em;
        font-weight: bold;
        color: #333;
        padding: 0 10px;
    }
    .piece {
        margin: 5px;
        cursor: pointer;
    }
    .piece td {
        width: 10px;
        height: 10px;
        text-align: center;
    }
    #selected {
        height: 90px;
        overflow-x: auto; /* Keep this for when there are more than 12 tables */
        white-space: nowrap;
        display: flex;
        justify-content: center; /* This is the key change */
        align-items: center;
    }
    .centered-container {
        width: 100%;
        display: flex;
        justify-content: center;
        margin-bottom: 20px;
    }
    #sol {
        display: flex;
        flex-direction: column;
        align-items: center;
    }
    .solution {
        margin-bottom: 10px;
    }
    .boardRow {
        border-left: 5px solid;
    }
    .boardRow td  {
        border: 1px dashed #CCCCCC;
    }
    #boardSize {
        width: 564px;
        height: 248px;
        margin: 0px 140px 0px 140px;
    }
    #boardSize .selectedSize:not(.bx) {
        border-right: 5px solid !important;
    }
    .boardSizeSelector {
        cursor: pointer;
    }
    .upTo {
        border-top: 5px solid !important;
    }
    .downTo {
        border-bottom: 5px solid !important;
    }

    .solutions-button {
        margin: 20px;
        width: 450px;
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        padding: 15px 30px;
        border-radius: 10px;
        border: 5px solid #000000;
        background-color: #469fd7;
        color: #000000;
        font-family: Arial, sans-serif;
        cursor: pointer;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.2);
        transition: background-color 0.3s ease, transform 0.2s ease;
    }

    .solutions-button:hover {
        background-color: #4b7bba;
        transform: translateY(-2px);
    }

    .solutions-button:active {
        transform: translateY(0); /* Press down effect */
    }

    .faq-button {
        margin: 20px;
        width: 50px;
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        padding: 15px 30px;
        border-radius: 10px;
        border: 5px solid #000000;
        background-color: #469fd7;
        color: #000000;
        font-family: Arial, sans-serif;
        cursor: pointer;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.2);
        transition: background-color 0.3s ease, transform 0.2s ease;
    }

    .faq-button:hover {
        background-color: #4b7bba;
        transform: translateY(-2px);
    }

    .faq-button:active {
        transform: translateY(0); /* Press down effect */
    }


    .main-text {
        font-size: 1.6em;
        font-weight: bold;
    }

    .sub-text {
        font-size: 0.7em;
        font-style: italic;
        opacity: 0.8;
        margin-top: 5px; /* Adds space between the main and subtext */
    }

    .modal {
        display: none;
        position: fixed;
        z-index: 1;
        left: 0;
        top: 0;
        width: 100%;
        height: 100%;
        background-color: rgba(0, 0, 0, 0.4);
        justify-content: center;
        align-items: center;
    }

    .modal-content {
        background-color: #fff;
        padding: 20px;
        border-radius: 10px;
        box-shadow: 0 5px 15px rgba(0, 0, 0, 0.3);
        width: 90%;
        max-width: 600px;
        position: relative;
        max-height: 80vh;
        overflow-y: auto;
    }

    .close-btn {
        color: #aaa;
        float: right;
        font-size: 28px;
        font-weight: bold;
        cursor: pointer;
    }

    .close-btn:hover,
    .close-btn:focus {
        color: black;
        text-decoration: none;
        cursor: pointer;
    }

    .faq-container {
        padding-top: 20px;
    }

    .faq-question {
        width: 100%;
        background-color: #f9f9f9;
        color: #444;
        cursor: pointer;
        padding: 18px;
        border: none;
        text-align: left;
        outline: none;
        font-size: 15px;
        transition: 0.4s;
        border-bottom: 1px solid #ddd;
        display: flex;
        justify-content: space-between;
        align-items: center;
    }

    .faq-question:hover {
        background-color: #e9e9e9;
    }

    .faq-icon {
        font-weight: bold;
        transition: transform 0.3s ease;
    }

    .faq-question.active .faq-icon {
        transform: rotate(45deg);
    }

    .faq-answer {
        background-color: white;
        color: #444;
        max-height: 0;
        overflow: hidden;
        transition: max-height 0.4s ease-out;
        padding: 0 18px;
        }

    .faq-answer p {
        padding: 10px 0;
        margin: 0;
    }

    .faq-question.active + .faq-answer {
        max-height: 200px;
    }


</style>
"""

pieces = (
    # Blue
    [
        [1, 1, 1, 1, 1],
    ],
    # pink
    [
        [2, 2],
        [2, 2],
        [0, 2],
    ],
    # # turcoise
    [
        [3, 3, 0],
        [0, 3, 0],
        [0, 3, 3],
    ],
    # light green
    [
        [4, 0, 0],
        [4, 4, 0],
        [0, 4, 4],
    ],
    # purple
    [
        [5, 5, 0, 0],
        [0, 5, 5, 5],
    ],
    # light blue
    [
        [6, 0, 0],
        [6, 0, 0],
        [6, 6, 6],
    ],
    # yellow
    [
        [7, 0, 7],
        [7, 7, 7],
    ],
    # green
    [
        [0, 8, 0],
        [0, 8, 0],
        [8, 8, 8],
    ],
    # red
    [
        [0, 9, 0],
        [9, 9, 9],
        [0, 9, 0],
    ],
    # orange
    [
        [10, 10],
        [0, 10],
        [0, 10],
        [0, 10],
    ],
    # Brown
    [
        [0, 11],
        [11, 11],
        [0, 11],
        [0, 11],
    ],
    # light pink
    [
        [0, 12, 12],
        [12, 12, 0],
        [0, 12, 0],
    ],
)


def draw(board):
    piece = max(board[0])
    sol = f'<table class="piece" id="p{piece}" data-piece-id="{piece}">\n'
    for y, row in enumerate(board):
        sol += f"<tr>"
        for x, col in enumerate(row):
            border_classes = ""
            if not board[y][x] == 0:
                if x > 0 and board[y][x - 1] != col or x == 0:
                    border_classes += " bl"
                if (
                    x < len(board[y]) - 1
                    and board[y][x + 1] != col
                    or x == len(board[y]) - 1
                ):
                    border_classes += " br"
                if y > 0 and board[y - 1][x] != col or y == 0:
                    border_classes += " bt"
                if y < len(board) - 1 and board[y + 1][x] != col or y == len(board) - 1:
                    border_classes += " bb"
            sol += f'<td class="b{col} {border_classes}"></td>'
        sol += "</tr>\n"
    sol += "</table>\n"
    return sol


with open("all_solutions.json", "r") as sols:
    solutions = [json.loads(l) for l in sols.readlines() if l]

deadends = []
for x in [3, 4, 5, 6, 7, 8, 9, 10, 11, 12]:
    with open(f"iterations_{x}.json") as its:
        for l in its.readlines():
            if l:
                deadends.append(json.loads(l))
deadends = json.dumps(deadends)

drawn_pieces = [draw(p) for p in pieces]
# with open(f"all_solutions.html", "w") as sol:
#     sol.write(style)

# for s in solutions:
#     draw(s)


body = f"""
    <div class="container">
        <h1 style="float: left">Ultimate Katamino Solver</h1>
        <button id="openModalBtn" style="float: right;" class="faq-button">FAQ</button>
    </div>

    <fieldset class="pieces-fieldset">
        <legend>Which pieces do you want to use?</legend>
        <div class="container" id="pieces">
        {"".join(drawn_pieces)}
        </div>
    </fieldset>
    <fieldset class="pieces-fieldset">
        <legend>Selected pieces:</legend>
        <div class="container" id="selected">
        </div>
    </fieldset>
    <fieldset class="board-fieldset">
        <legend>Board size:</legend>
        <div class="container">
        <table id="boardSize">
            <tr class="boardRow">
                <td class="c1"></td>
                <td class="c2"></td>
                <td class="c3 boardSizeSelector"></td>
                <td class="c4 boardSizeSelector"></td>
                <td class="c5 boardSizeSelector"></td>
                <td class="c6 boardSizeSelector"></td>
                <td class="c7 boardSizeSelector"></td>
                <td class="c8 boardSizeSelector"></td>
                <td class="c9 boardSizeSelector"></td>
                <td class="c10 boardSizeSelector"></td>
                <td class="c11 boardSizeSelector"></td>
                <td class="c12 boardSizeSelector"></td>
            </tr>
            <tr class="boardRow">
                <td class="c1"></td>
                <td class="c2"></td>
                <td class="c3 boardSizeSelector"></td>
                <td class="c4 boardSizeSelector"></td>
                <td class="c5 boardSizeSelector"></td>
                <td class="c6 boardSizeSelector"></td>
                <td class="c7 boardSizeSelector"></td>
                <td class="c8 boardSizeSelector"></td>
                <td class="c9 boardSizeSelector"></td>
                <td class="c10 boardSizeSelector"></td>
                <td class="c11 boardSizeSelector"></td>
                <td class="c12 boardSizeSelector"></td>
            </tr>
            <tr class="boardRow">
                <td class="c1"></td>
                <td class="c2"></td>
                <td class="c3 boardSizeSelector"></td>
                <td class="c4 boardSizeSelector"></td>
                <td class="c5 boardSizeSelector"></td>
                <td class="c6 boardSizeSelector"></td>
                <td class="c7 boardSizeSelector"></td>
                <td class="c8 boardSizeSelector"></td>
                <td class="c9 boardSizeSelector"></td>
                <td class="c10 boardSizeSelector"></td>
                <td class="c11 boardSizeSelector"></td>
                <td class="c12 boardSizeSelector"></td>
            </tr>
            <tr class="boardRow">
                <td class="c1"></td>
                <td class="c2"></td>
                <td class="c3 boardSizeSelector"></td>
                <td class="c4 boardSizeSelector"></td>
                <td class="c5 boardSizeSelector"></td>
                <td class="c6 boardSizeSelector"></td>
                <td class="c7 boardSizeSelector"></td>
                <td class="c8 boardSizeSelector"></td>
                <td class="c9 boardSizeSelector"></td>
                <td class="c10 boardSizeSelector"></td>
                <td class="c11 boardSizeSelector"></td>
                <td class="c12 boardSizeSelector"></td>
            </tr>
            <tr class="boardRow">
                <td class="c1"></td>
                <td class="c2"></td>
                <td class="c3 boardSizeSelector"></td>
                <td class="c4 boardSizeSelector"></td>
                <td class="c5 boardSizeSelector"></td>
                <td class="c6 boardSizeSelector"></td>
                <td class="c7 boardSizeSelector"></td>
                <td class="c8 boardSizeSelector"></td>
                <td class="c9 boardSizeSelector"></td>
                <td class="c10 boardSizeSelector"></td>
                <td class="c11 boardSizeSelector"></td>
                <td class="c12 boardSizeSelector"></td>
            </tr>
            <tr>
                <td class="bx">1</td>
                <td class="bx ">2</td>
                <td class="bx boardSizeSelector c3">3</td>
                <td class="bx boardSizeSelector c4">4</td>
                <td class="bx boardSizeSelector c5">5</td>
                <td class="bx boardSizeSelector c6">6</td>
                <td class="bx boardSizeSelector c7">7</td>
                <td class="bx boardSizeSelector c8">8</td>
                <td class="bx boardSizeSelector c9">9</td>
                <td class="bx boardSizeSelector c10">10</td>
                <td class="bx boardSizeSelector c11">11</td>
                <td class="bx boardSizeSelector c12">12</td>
            </tr>
        </table>
        </div>
    </fieldset>

    <div class="centered-container">
        <button class="solutions-button" id="getSolutions">
          <span class="main-text">Get all 1000 solution</span>
          <span class="sub-text">out of 10000 dead ends</span>
        </button>

    </div>

    <div class="table-list" id="sol">
    </div>

    <div id="faqModal" class="modal">
        <div class="modal-content">
            <span class="close-btn">&times;</span>
            <div class="faq-container">
                <h2>Frequently Asked Questions</h2>
                
                <div class="faq-item">
                    <button class="faq-question">
                        <span>Q1: Why?</span>
                        <span class="faq-icon">+</span>
                    </button>
                    <div class="faq-answer">
                        <p>"Science isn't about WHY. It's about <a href="https://i1.theportalwiki.net/img/a/a5/Cave_Johnson_fifties_fifth_test_complete09.wav" target="blank">WHY NOT</a>." (JOHNSON, Cave) .</p>
                    </div>
                </div>

                <div class="faq-item">
                    <button class="faq-question">
                        <span>Q2: Isn't the purpose of the game to solve the puzzle? Isn't this cheating?</span>
                        <span class="faq-icon">+</span>
                    </button>
                    <div class="faq-answer">
                        <p>Yes, it is. Yet here you are. I've solved all the puzzle and put all the answers here. What is YOUR excuse for being here?</p>
                    </div>
                </div>
                
                <div class="faq-item">
                    <button class="faq-question">
                        <span>Q3: How does this website solves all the possible configurations?</span>
                        <span class="faq-icon">+</span>
                    </button>
                    <div class="faq-answer">
                        <p>Well, it doesn't. It already have all the possible answers. You are just searching for the ones you want.</p>
                    </div>
                </div>

                <div class="faq-item">
                    <button class="faq-question">
                        <span>Q4: Did you solve all the challenges?</span>
                        <span class="faq-icon">+</span>
                    </button>
                    <div class="faq-answer">
                        <p>Kinda. I wrote the software. The software solved it.</p>
                    </div>
                </div>

                <div class="faq-item">
                    <button class="faq-question">
                        <span>Q5: But how?</span>
                        <span class="faq-icon">+</span>
                    </button>
                    <div class="faq-answer">
                        <p>Brute force. No brains, just brute force.</p>
                    </div>
                </div>

                <div class="faq-item">
                    <button class="faq-question">
                        <span>Q6: How long did it take?</span>
                        <span class="faq-icon">+</span>
                    </button>
                    <div class="faq-answer">
                        <p>Less than you would think and more than I would like to admit.</p>
                    </div>
                </div>

                <div class="faq-item">
                    <button class="faq-question">
                        <span>Q7: Can I download all the solutions?</span>
                        <span class="faq-icon">+</span>
                    </button>
                    <div class="faq-answer">
                        <p>Sure, be my guest. <a href="https://github.com/nano-labs/katamino" target="blank">It is all here</a></p>
                    </div>
                </div>

            </div>
        </div>
    </div>


"""
with open("js.js", "r") as js:
    script = f"""
    <script type="text/javascript">

     solutions = {solutions};
     deadends = {deadends};

     {js.read()}
    </script>
    """
html = f"""
<!DOCTYPE html>
<html>
    <head>
        <meta charset="utf-8">
        <title>Ultimate Katamino Solver</title>
        {style}
    </head>
    <body>
    {body}
    {script}
    </body>
</html>"""

with open("index.html", "w") as sols:
    sols.write(html)
