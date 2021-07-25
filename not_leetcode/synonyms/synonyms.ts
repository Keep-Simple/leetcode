import fs from 'fs/promises'
import path from 'path'

const answerSynonymsQueries = (inputLines: string[]): string[] => {
    const testCases = +inputLines.shift()
    const finalAnswers: string[] = []

    for (let i = 0; i < testCases; i++) {
        const dictionaryLenght = +inputLines.shift()
        const dictionary = inputLines.splice(0, dictionaryLenght)

        const synonymsSets: Set<string>[] = []

        dictionary.forEach((line) => {
            const twoWords = line.split(' ')
            let foundInSetWithIdx = -1

            synonymsSets.forEach((set, idx) => {
                const isAlreadyThere =
                    set.has(twoWords[0]) || set.has(twoWords[1])

                if (isAlreadyThere) {
                    if (foundInSetWithIdx === -1) {
                        twoWords.forEach(set.add, set)
                    } else {
                        // concat two sets
                        synonymsSets[foundInSetWithIdx].forEach(set.add, set)
                        synonymsSets.splice(foundInSetWithIdx, 1)
                    }
                    foundInSetWithIdx = idx
                }
            })

            if (foundInSetWithIdx === -1) {
                synonymsSets.push(new Set(twoWords))
            }
        })

        // dictionary is created, now we can answer tests

        const queriesLength = +inputLines.shift()
        const queries = inputLines.splice(0, queriesLength)

        const answersArray = queries.map((query) => {
            const twoQueryWords = query.split(' ')

            if (twoQueryWords[0] === twoQueryWords[1]) {
                return 'synonyms'
            } else {
                const hasFound = synonymsSets.some(
                    (set) =>
                        set.has(twoQueryWords[0]) && set.has(twoQueryWords[1])
                )

                return hasFound ? 'synonyms' : 'different'
            }
        })

        finalAnswers.push(...answersArray)
    }

    return finalAnswers
}

export async function runSynonymsTask(inputFile: string, outputFile: string) {
    try {
        // read input
        const data = await fs.readFile(getExampleFilesDir(inputFile))
        const inputLines: string[] = data.toString().toLowerCase().split('\n')

        const finalAnswers = answerSynonymsQueries(inputLines)

        // write answer
        await fs.writeFile(getTestFilesDir(outputFile), finalAnswers.join('\n'))
    } catch (e) {
        console.error(e)
    }
}

export function getExampleFilesDir(fileName?: string) {
    return path.resolve(__dirname, 'example_files', fileName || '')
}

export function getTestFilesDir(fileName?: string) {
    return path.resolve(__dirname, 'test_files', fileName || '')
}
