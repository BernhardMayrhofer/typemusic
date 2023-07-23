from mido import MidiFile, MidiFile, MidiTrack

# Opening the original MIDI sequence
input_midi = MidiFile('midi/canon-3.mid')

f = open('midi/canon-3.txt', "a")
f.write(str(input_midi))
f.close()

# Creating the destination file object
#output_midi = MidiFile()

# Copying the time metrics between both files
#output_midi.ticks_per_beat = input_midi.ticks_per_beat

#note_map = {}
# Load the mapping file
#with open('note_map.csv') as map_text:
#    for line in map_text:
#        elements = line.replace('\n','').split(',')
#        # Each line in the mapping file will be loaded into a
#        # dictionary with the original MIDI note as key and
#        # another dictionary with target note 
#        # and description as value
#        note_map[int(elements[0])] = { 
#            'target_note': int(elements[1]), 
#            'description': elements[2] }'