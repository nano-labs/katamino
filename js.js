
var selectedPieces = [];
var boardSize = 3;

function render(s) {
    const solutiondiv = document.createElement('div')
    const hr = document.createElement('hr')
    const table = document.createElement('table');
    solutiondiv.classList.add("solution");
    const rows = s.length;
    const cols = s[0].length;

    for (let i = 0; i < rows; i++) {
        const tr = document.createElement('tr');
        for (let j = 0; j < cols; j++) {
            const td = document.createElement('td');
            const value = s[i][j];
            let classes = `b${value}`;

            if (i === 0 || value !== s[i - 1][j]) {
                classes += ' bt';
            }
            if (i === rows - 1 || value !== s[i + 1][j]) {
                classes += ' bb';
            }
            if (j === 0 || value !== s[i][j - 1]) {
                classes += ' bl';
            }
            if (j === cols - 1 || value !== s[i][j + 1]) {
                classes += ' br';
            }

            td.className = classes;
            tr.appendChild(td);
        }
        table.appendChild(tr);
    }

    const xLabelsRow = document.createElement('tr');
    for (let j = 0; j < cols; j++) {
        xLabelsRow.innerHTML += `<td class="bx">${j + 1}</td>`;
    }
    table.appendChild(xLabelsRow);

    solutiondiv.appendChild(table)
    document.getElementById('sol').appendChild(solutiondiv);
}

function clearSolutions() {
    document.getElementById('sol').innerHTML = "";
}

function findSolutions(numbers, xsize) {

    if (xsize == 0) {
        solutionsWithXsize = solutions;
    } else {
        solutionsWithXsize = solutions.filter(solution => solution[0].length === xsize);
    }

    return solutionsWithXsize.filter(solution => {
        const allNumbersInSolution = solution.flat();
        const tempSolutionNumbers = [...allNumbersInSolution];
    
        return numbers.every(num => {
            const index = tempSolutionNumbers.indexOf(num);
            if (index !== -1) {
                tempSolutionNumbers.splice(index, 1);
            return true;
            }
        return false;
    });
  });
}
function findDeadEnds(numbers, xsize) {
  const matchingItems = deadends.filter(item => {
    const barAtMatches = item.bar_at === xsize;
    const piecesSetContainsPieces = numbers.every(piece =>
      item.pieces_set.includes(piece)
    );

    return barAtMatches && piecesSetContainsPieces;
  });

  const totalIterations = matchingItems.reduce(
    (sum, item) => sum + item.iterations,
    0
  );

  return totalIterations;
}


function renderFilter(numbers, xsize) {
    sols = findSolutions(numbers, xsize);
    if (sols.length == 0) {
        return;
    }
    if (sols !== undefined && sols.length > 200) {
        if (confirm("There are " + sols.length + " that match this. Are you sure you want me to show all of them?") == false) {
            return
        }
    }
    clearSolutions();
    sols.forEach(solution => {
        render(solution);
    });
}
function addPiece(p) {
    if (selectedPieces.includes(p)) {
        removePiece(p);
    } else {
        selectedPieces.push(p)
        selectedPieces = [...new Set(selectedPieces)];
        if (selectedPieces.length > boardSize) {
            setBoardSize(selectedPieces.length);
        }        
    }
    refreshSelected();
    changeButton();
}
function removePiece(p) {
    selectedPieces = selectedPieces.filter(i => i !== p);
    refreshSelected();
    changeButton();
}
function refreshSelected() {
    const piecesDiv = document.getElementById('pieces');
    const selectedPiecesDiv = document.getElementById('selected');
    selectedPiecesDiv.innerHTML = '';

    selectedPieces.forEach(id => {
        const originalElement = document.getElementById("p" + id);

        const clonedElement = originalElement.cloneNode(true);      
        clonedElement.removeAttribute('id');
        selectedPiecesDiv.appendChild(clonedElement);
        clonedElement.addEventListener("click", function() {
            removePiece(parseInt(this.dataset.pieceId));
        })
    });    
}

document.getElementById('p1').addEventListener('click', function() { addPiece(1) });
document.getElementById('p2').addEventListener('click', function() { addPiece(2) });
document.getElementById('p3').addEventListener('click', function() { addPiece(3) });
document.getElementById('p4').addEventListener('click', function() { addPiece(4) });
document.getElementById('p5').addEventListener('click', function() { addPiece(5) });
document.getElementById('p6').addEventListener('click', function() { addPiece(6) });
document.getElementById('p7').addEventListener('click', function() { addPiece(7) });
document.getElementById('p8').addEventListener('click', function() { addPiece(8) });
document.getElementById('p9').addEventListener('click', function() { addPiece(9) });
document.getElementById('p10').addEventListener('click', function() { addPiece(10) });
document.getElementById('p11').addEventListener('click', function() { addPiece(11) });
document.getElementById('p12').addEventListener('click', function() { addPiece(12) });

// function selectPiece1(event, element) { addPiece(1); }
// function selectPiece2(event, element) { addPiece(2); }
// function selectPiece3(event, element) { addPiece(3); }
// function selectPiece4(event, element) { addPiece(4); }
// function selectPiece5(event, element) { addPiece(5); }
// function selectPiece6(event, element) { addPiece(6); }
// function selectPiece7(event, element) { addPiece(7); }
// function selectPiece8(event, element) { addPiece(8); }
// function selectPiece9(event, element) { addPiece(9); }
// function selectPiece10(event, element) { addPiece(10); }
// function selectPiece11(event, element) { addPiece(11); }
// function selectPiece12(event, element) { addPiece(12); }

function setBoardSize(s) {
    boardSize = s;
    var col = ".c" + s;
    document.querySelectorAll('.selectedSize').forEach(element => {
        element.classList.remove('selectedSize');
    });
    document.querySelectorAll(col).forEach(element => {
        element.classList.add('selectedSize');
    });

    document.querySelectorAll('.upTo').forEach(element => {
        element.classList.remove('upTo');
    });
    firstRow = document.getElementById('boardSize').querySelector('tr');
    cells = firstRow.querySelectorAll('td')
    for (let i = 0; i < s && i < cells.length; i++) {
        cells[i].classList.add('upTo');
    }

    document.querySelectorAll('.downTo').forEach(element => {
        element.classList.remove('downTo');
    });
    lastRow = document.getElementById('boardSize').rows[4];
    cells = lastRow.querySelectorAll('td');
    for (let i = 0; i < s && i < cells.length; i++) {
        cells[i].classList.add('downTo');
    }
    changeButton()
}
function changeButton() {
    solCount = findSolutions(selectedPieces, boardSize).length;
    de = findDeadEnds(selectedPieces, boardSize);
    if (solCount == 0) {
        document.getElementById('getSolutions').querySelector(".main-text").innerText = "There are no solutions for this setup";
        document.getElementById('getSolutions').querySelector(".sub-text").innerText = "only " + de.toLocaleString() + " dead ends";
    } else {
        document.getElementById('getSolutions').querySelector(".main-text").innerText = "Get all " + solCount + " solutions";
        document.getElementById('getSolutions').querySelector(".sub-text").innerText = "out of " + de.toLocaleString() + " dead ends";
    }
};
document.getElementById("getSolutions").addEventListener("click", function() {
    renderFilter(selectedPieces, boardSize);
});


document.querySelectorAll(".c3").forEach(block => {
    block.addEventListener('click', function() {
        setBoardSize(3);
    });
});
document.querySelectorAll(".c4").forEach(block => {
    block.addEventListener('click', function() {
        setBoardSize(4);
    });
});
document.querySelectorAll(".c5").forEach(block => {
    block.addEventListener('click', function() {
        setBoardSize(5);
    });
});
document.querySelectorAll(".c6").forEach(block => {
    block.addEventListener('click', function() {
        setBoardSize(6);
    });
});
document.querySelectorAll(".c7").forEach(block => {
    block.addEventListener('click', function() {
        setBoardSize(7);
    });
});
document.querySelectorAll(".c8").forEach(block => {
    block.addEventListener('click', function() {
        setBoardSize(8);
    });
});
document.querySelectorAll(".c9").forEach(block => {
    block.addEventListener('click', function() {
        setBoardSize(9);
    });
});
document.querySelectorAll(".c10").forEach(block => {
    block.addEventListener('click', function() {
        setBoardSize(10);
    });
});
document.querySelectorAll(".c11").forEach(block => {
    block.addEventListener('click', function() {
        setBoardSize(11);
    });
});
document.querySelectorAll(".c12").forEach(block => {
    block.addEventListener('click', function() {
        setBoardSize(12);
    });
});

setBoardSize(3);

const modal = document.getElementById('faqModal');
const openModalBtn = document.getElementById('openModalBtn');
const closeBtn = document.getElementsByClassName('close-btn')[0];
const faqQuestions = document.querySelectorAll('.faq-question');

openModalBtn.addEventListener('click', () => {
    modal.style.display = 'flex';
});

closeBtn.addEventListener('click', () => {
    modal.style.display = 'none';
});

window.addEventListener('click', (event) => {
    if (event.target === modal) {
        modal.style.display = 'none';
    }
});

faqQuestions.forEach(question => {
    question.addEventListener('click', () => {
        question.classList.toggle('active');

        const answer = question.nextElementSibling;
        
        if (answer.style.maxHeight) {
            answer.style.maxHeight = null;
        } else {
            answer.style.maxHeight = answer.scrollHeight + 'px';
        }
    });
});