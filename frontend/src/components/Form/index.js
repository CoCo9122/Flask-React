import React, { useContext } from 'react'
import ContextSocket from '../../context/context-socketio'

import { Box, Stack, VStack, HStack, Flex, Text, Button } from '@chakra-ui/react'

const Form = () => {
    const {Socket} = useContext(ContextSocket)
    const sendMessage = () => {
        Socket.emit("message", "Hello world")
        console.log("Hello world!")
    }
    return (
        <Box>
            <Button onClick={() => sendMessage()}>CLICK</Button>
        </Box>
    )
}

export default Form